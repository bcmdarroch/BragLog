# /usr/bin/env python
# download twilio-python library

import os
from twilio.rest import Client

# test credentials
account_sid = os.environ["TWILIO_SID_TEST"]
auth_token = os.environ["TWILIO_TOKEN_TEST"]
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
    to=os.environ["BEC_NUMBER"],
    from_=os.environ["TWILIO_NUMBER_TEST"],
    body="Testing brag log heeeey"
)

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
