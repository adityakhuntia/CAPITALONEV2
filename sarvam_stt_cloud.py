import requests
import os
import json 

API_URL = "https://api.sarvam.ai/speech-to-text-translate"
API_KEY = "sk_0w5etw1v_MYYLiMqU4Z1XG02MS74LiYA9"

def speech_to_text_translate(file_path: str, target_lang: str = "en-IN", model: str = "saaras:v2.5"):
    """
    Translate speech from an audio file into target language text using Sarvam API.
    
    :param file_path: Path to the audio file (must be wav/pcm 16kHz mono)
    :param target_lang: Target language code (default "en-IN")
    :param model: Model name ("saaras:v1", "saaras:v2", "saaras:v2.5", "saaras:turbo", "saaras:flash")
    :return: JSON response from API
    """
    headers = {"api-subscription-key": API_KEY}

    with open(file_path, "rb") as f:
        files = {
            "file": (os.path.basename(file_path), f, "audio/wav")
        }
        data = {
            "target_language_code": target_lang,
            "model": model
        }
        response = requests.post(API_URL, headers=headers, files=files, data=data)

    # Return parsed JSON or error info
    try:
        return response.json()
    except Exception:
        return {"status_code": response.status_code, "error": response.text}


# Example usage:
#result = speech_to_text_translate("/Users/adityakhuntia/Desktop/CAPITAL ONE/audio_8.wav")
#print(json.dumps(result))
