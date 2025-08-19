import requests, time
import os
from dotenv import load_dotenv

from audio_flow import pipeline
from sarvam_stt_cloud import speech_to_text_translate
from whatsapp import send_whatsapp_message


load_dotenv()
# from audio_flow import process_audio
# from rag_flow import process_rag

BASE_URL = "https://flask-whatsapp-webhook.onrender.com"

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")


import subprocess, os

def convert_to_wav(input_path):
    output_path = os.path.splitext(input_path)[0] + ".wav"
    cmd = ["ffmpeg", "-y", "-i", input_path, "-ar", "16000", "-ac", "1", output_path]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_path




def download_audio(media_url, save_path="audio.ogg"):
    if not ACCOUNT_SID or not AUTH_TOKEN:
        raise ValueError("Twilio credentials not found in environment variables")
    
    # follow redirects explicitly
    resp = requests.get(
        media_url,
        auth=(ACCOUNT_SID, AUTH_TOKEN),
        timeout=15,
        allow_redirects=True
    )
    resp.raise_for_status()

    with open(save_path, "wb") as f:
        for chunk in resp.iter_content(1024):
            f.write(chunk)
    return save_path



def get_media_type(media_url):
    try:
        resp = requests.get(
            media_url,
            auth=(ACCOUNT_SID, AUTH_TOKEN),
            timeout=10,
            allow_redirects=True,
            stream=True  # don’t download the whole file
        )
        resp.raise_for_status()
        return resp.headers.get("Content-Type", "")
    except Exception as e:
        print("Error fetching media type:", e)
        return ""




def scheduler():
    while True:
        try:
            resp = requests.get(f"{BASE_URL}/messages")
            resp.raise_for_status()
            messages = resp.json()

            for msg in messages:
                if msg.get("seen"):
                    continue

                user_lang = msg.get("language")
                user_state = msg.get("state")
                print(f"User Lang: {user_lang}, State: {user_state}")

                
                from_number = msg.get("from") or msg.get("From")
                # Remove 'whatsapp:' prefix if present
                if from_number and from_number.startswith("whatsapp:"):
                    from_number = from_number.replace("whatsapp:", "")

                print(msg)
                media_url = msg.get("media_url")
                body = msg.get("body", "")

                if media_url:
                    media_type = get_media_type(media_url)

                    if media_type.startswith("audio"):
                        print(f"[AUDIO] Processing message {msg}")
                        local_file = download_audio(media_url, f"audio_{msg['id']}.ogg")
                        if local_file:
                            try:
                                wav_file = convert_to_wav(local_file)
                                result = speech_to_text_translate(wav_file)
                                print(result)

                                
                                #OFFLINE VERSION
                                #audio_pipline_result = pipeline(wav_file)
                                #prompt = audio_pipline_result['Translation']



                                ## SEND TO RAG PIPELINE AND GET A RESPONSE SHIT 
                                

                                ##ACESS USERS LANGUAGE FOR TRANSLATING THE REPLY 


                                ## SEND A REPLY TO THE MAN
                                query = result['transcript']
                                recipient = from_number
                                response = "ANIK RAG BANA DE"
                                recipient = "+918287724256"
                                sid = send_whatsapp_message(query, response, recipient)
                                print("Message SID:", sid)


                            finally:
                                print("FILE REMOVED")


                            

                            
                            # process_audio(local_file)
                            #os.remove(local_file)

                    elif media_type.startswith("image") or body:
                        print(f"[RAG] Processing message {msg}")
                        # process_rag(body, media_url)

                elif body:
                    print(f"[RAG] Processing text-only message {msg}")
                    # process_rag(body)

                # ✅ Mark as seen
                seen_url = f"{BASE_URL}/messages/{msg['id']}/seen"
                r = requests.post(seen_url)
                if r.status_code == 200:
                    print(f"Marked message {msg['id']} as seen")

        except Exception as e:
            print("Error in scheduler:", e)

        time.sleep(30)

if __name__ == "__main__":
    scheduler()
