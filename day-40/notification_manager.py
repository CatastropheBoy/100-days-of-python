from twilio.rest import Client

class NotificationManager:
    
    def __init__(self, sid, token) -> None:
        self.sid = sid
        self.token = token


    def send_message(self, msg):
        client = Client(self.sid, self.token)
        message = client.messages \
                    .create(
                            body= msg,
                            from_='+13218061994',
                            to='+14156225197'
                    )

        return message.status