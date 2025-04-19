from twilio.rest import Client
account_sid = 'AC662cd859b19409a707668de92be52b98'
auth_token = 'c40c79c686c4dc0904497d66ed0eac09'
client = Client(account_sid, auth_token)
def sendSms():
    message = client.messages.create(
    from_='+12696651024',
    body='Alert! Intruder Detected!',
    to='+919045141758'
    )

    print(message.sid)