from twilio.rest import Client
import json

import os
from dotenv import load_dotenv

load_dotenv()
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")


def send_whatsapp_message(query_text: str, response_text: str, recipient_number: str) -> str:
   
    account_sid = TWILIO_SID
    auth_token = TWILIO_AUTH

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_="whatsapp:+14155238886",  # Your Twilio WhatsApp number
        content_sid="HXefedabcd9c84502ca04997bf045c90f9",  # WhatsApp template SID
        content_variables=json.dumps({
            "Query": query_text,       # replaces {{1}} in template
            "Response": response_text     # replaces {{2}} in template
        }),
        to=f"whatsapp:{recipient_number}"
    )

    return message.sid


# Example usage:
#if __name__ == "__main__":
#    query = "किसान मित्र 🌾"
#    response = "आज की सलाह: खेत की सिंचाई शाम 4 बजे करें।"
#    recipient = "+919818851259"
#    sid = send_whatsapp_message(query, response, recipient)
#    print("Message SID:", sid)



   