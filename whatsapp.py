from twilio.rest import Client
import json

def send_whatsapp_message(query_text: str, response_text: str, recipient_number: str) -> str:
    """
    Sends a WhatsApp message using Twilio's Content API template.

    Args:
        query_text (str): The incoming query text (to fill template variable {{1}})
        response_text (str): The response/advice text (to fill template variable {{2}})
        recipient_number (str): Recipient's WhatsApp number in format '+91XXXXXXXXXX'

    Returns:
        str: The SID of the sent message
    """
    account_sid = "TWILIO_ACCOUNT_SID_REMOVED"
    auth_token = "c45bbb4dac14fd3fab6be849920322ce"

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
