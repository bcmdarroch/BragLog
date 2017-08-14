import os
import sched
import time
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


def test():
    for message in client.messages.list():
        print(message.from_)


s = sched.scheduler(time.time, time.sleep)


# def do_something(sc):
#     print "Doing stuff..."
#     date_sent()
#     s.enter(4, 1, do_something, (sc,))
#
#
# s.enter(4, 1, do_something, (s,))
# s.run()


# def test():
#     number_array = []
#     message_object_array = client.messages.list()
#     for message in message_object_array:
#         if message.direction == 'inbound' and message.from_ not in number_array:
#             number_array.append(message.from_)
#     return number_array
#
#
# print test()
# print "TIME STAMP:"
print date_sent()
# print "MESSAGES FROM MEEEE:"
print messages_from_me()
# print "FROM TEST:"
# print test()
# print client.messages.list()
# print time.localtime(time.time())
