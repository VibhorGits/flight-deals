from twilio.rest import Client

TWILIO_SID = "AC0e3d9ddc66af5411934c7b3f8d46b7c0"
TWILIO_AUTH_TOKEN = "c269bfd6fa87f13137d2bbfc57054554"
TWILIO_VIRTUAL_NUMBER = "+13204131570"
TWILIO_VERIFIED_NUMBER = "+917060254455"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
