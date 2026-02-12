#! python3
# textMyself.py - Defines the textMyself function that texts a message
# passed to it as a string

from twilio.rest import Client

# Preset values:
accountSID = 'Axxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxx'
myNumber = '+2349059289758'
twilioNumber = '+14133596142'


def textMyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)


textMyself('-')
