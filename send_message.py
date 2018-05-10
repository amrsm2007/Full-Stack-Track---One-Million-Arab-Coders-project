from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC219fb3b27f063b3ef52336e68492f5b5"
# Your Auth Token from twilio.com/console
auth_token  = "9d617057d897d16776f9044f095f24c5"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+966544684709",
    from_="+14259709546",
    body="Hello from Python my name is Amr Ali i love you !")

print(message.sid)