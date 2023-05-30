import smtplib

from twilio.rest import Client

TWILIO_SID = "AC4898a7ab76609abb85e3bf414350c2ac"
TWILIO_AUTH_TOKEN = "762bf168e924f1c61ff985a4321e3b90"
TWILIO_VIRTUAL_NUMBER = "+13156311742"
TWILIO_VERIFIED_NUMBER = "+917060254455"
MY_EMAIL = "pythontestingapp123@gmail.com"
MY_PASSWORD = "njscuesrjescoegs"



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

    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
