import requests, os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

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


#url = "https://api.twilio.com/2010-04-01/Accounts/TWILIO_ACCOUNT_SID_REMOVED/Messages/MMb6b5e5592c1243ca9685a28eb07ac897/Media/ME53c8ec3f2fbb19027f03f3292feae79f"
#print("Media type:", get_media_type(url))
