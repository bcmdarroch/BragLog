#!../flask/bin/python

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def hello_monkey():
    """ Respond to incoming calls w text message """

    resp = MessagingResponse().message("Hey hey you logged a brag! Nice!!")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
