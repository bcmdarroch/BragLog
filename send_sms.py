# /usr/bin/env python
# download twilio-python library

import os
import sched
import time

from twilio.rest import Client

# credentials
account_sid = os.environ["TWILIO_SID"]
auth_token = os.environ["TWILIO_TOKEN"]
client = Client(account_sid, auth_token)

DELAY = 5
DELAY_WEEK = 42


def get_numbers():
    number_array = []
    message_object_array = client.messages.list()
    for message in message_object_array:
        if message.direction == 'inbound' and message.from_ not in number_array:
            number_array.append(message.from_)
    return number_array

# message = client.api.account.messages.create(
#     to=os.environ["BEC_NUMBER"],
#     from_=os.environ["TWILIO_NUMBER_TEST"],
#     body="Testing brag log heeeey"
# )


def welcome():
    # last priority.
    # send them one initial welcome message when we get new number from website
    pass


def brag_timer():
    # s = sched.scheduler(time.time, time.sleep)
    # s.enter(DELAY, 1, brag_reminder(get_numbers(), s), (s,))
    # s.enter(DELAY, 1, brag_log(s), (s,))
    # s.run()

    for i in range(0, 7):
        brag_reminder(get_numbers())
        time.sleep(5)

    brag_log()


# def brag_log(scheduler):
def brag_log():
    msg_by_num = {}
    for message in client.messages.list(): # array of all messages
        # for each number, send most recent 7 messages (0-7 index)

        if message.direction == 'inbound':
            if message.from_ not in msg_by_num.keys():
                msg_by_num[message.from_] = []

            # stores message in the number's array of messages
            msg_by_num[message.from_].append(message.body)
    print msg_by_num

    for number, messages in msg_by_num.items():
        messages = messages[0:7]
        newline = "\n"
        messages = newline.join(messages)
        # emojis = u'\U0001f483 \U0001f451 \u2728 \U0001f3c6'.encode('unicode_escape')

        client.api.account.messages.create(
            to=number,
            from_=os.environ["TWILIO_NUMBER"],
            body= "Here's what you accomplished this week! Nice!!!! \n" + messages
        )
    # scheduler.enter(DELAY_WEEK, 1, brag_log(scheduler), (scheduler,))


# s = sched.scheduler(time.time, time.sleep)


def brag_reminder(numbers):
    # send at certain time.
    # send to all numbers stored.
    for number in numbers:
        client.api.account.messages.create(
            to=number,
            from_=os.environ["TWILIO_NUMBER"],
            body="Send me your brag for the day!"
        )
    # scheduler.enter(DELAY, 1, brag_reminder(get_numbers(), scheduler), (scheduler,))


brag_timer()

# live credentials
# account_sid = os.environ["TWILIO_SID"]
# auth_token = os.environ["TWILIO_TOKEN"]
# client = Client(account_sid, auth_token)
#
# message = client.api.account.messages.create(
#     to=os.environ["BEC_NUMBER"],
#     from_=os.environ["TWILIO_NUMBER"],
#     body="Testing brag log heeeey"
# )
