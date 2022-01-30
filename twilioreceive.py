import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route('/conuhacks2022', methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()

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