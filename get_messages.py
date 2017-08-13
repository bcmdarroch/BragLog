import os
from twilio.rest import Client

account_sid = os.environ["TWILIO_SID"]
auth_token = os.environ["TWILIO_TOKEN"]
client = Client(account_sid, auth_token)


def date_sent():
    for message in client.messages.list():
        print(message.date_sent)


def messages_from_me():
    for message in client.messages.list():
        if message.direction == 'inbound':
            print message.body


print "TIME STAMP:"
print date_sent()
print "MESSAGES FROM MEEEE:"
print messages_from_me()
