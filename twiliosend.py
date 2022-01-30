import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Your Account SID from twilio.com/console
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
# Your Auth Token from twilio.com/console
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)
