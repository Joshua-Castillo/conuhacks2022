import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from pyrebaseConfig import db

app = Flask(__name__)


@app.route('/conuhacks', methods=['GET', 'POST'])
def sms_reply():
    inb_msg = request.form['Body'].lower().strip()
    resp = MessagingResponse()
    db.child("users").child(1).set({"msg": inb_msg})
    resp.message('They will come for you')
#    inb_msg = request.form['Body'].lower().strip()
#    resp = MessagingResponse()
#    if(inb_msg == "hi"):
#        msg = resp.message("hi")
#    else:
#        resp.message("else still hi, no image")
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
