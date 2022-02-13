# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ[ACd905c1d9bcd9af1e4e683e91b73fa]
# auth_token = os.environ[8404fbf17af041bf139b814d65b7b52e]
account_sid = "ACd905c1d9bcd9af1e4e683e91b73fa2b5"
auth_token  = "8404fbf17af041bf139b814d65b7b52e"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Your friend is in danger",
                     from_='+18126338977',
                     to='+14258983378'
                 )

print(message.sid)

