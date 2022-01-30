import os
from twilio.rest import Client

account_sid = 'AC1958c9ad4107ebb03a3b991300cdb77f'
auth_token = '160378deb34384ac8bd2dbb3e2989b78'

client = Client(account_sid, auth_token)

client.messages.create(
    to='+15147937367',
    from_='+18733010318',
    body="Hi, it's me you're looking for"
)