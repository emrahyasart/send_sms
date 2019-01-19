from twilio.rest import Client

account_sid = "A*******************************"
auth_token = "6********************************"
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+90505*******",
    from_="+15126*****",
    body="Hello from Python!")


print(message.sid)