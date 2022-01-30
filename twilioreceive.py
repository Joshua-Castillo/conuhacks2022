import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from pyrebaseConfig import db

app = Flask(__name__)


@app.route('/conuhacks', methods=['GET', 'POST'])
def sms_reply():
    inb_phone = request.form['From']
    inb_msg = request.form['Body'].lower().strip()

    resp = MessagingResponse()

    db.child("phoneIDs").child(inb_phone).set(inb_msg)
    # db.child("users").child(1).update({"msg": inb_msg, "phone": inb_phone})
    resp.message("got it!")

#    inb_msg = request.form['Body'].lower().strip()
#    resp = MessagingResponse()
#    if(inb_msg == "hi"):
#        msg = resp.message("hi")
#    else:
#        resp.message("else still hi, no image")

# 0. role
# 1.

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
