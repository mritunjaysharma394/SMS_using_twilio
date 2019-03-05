from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6d58c72d8142f49bf5b0616f2cdf0a08"
# Your Auth Token from twilio.com/console
auth_token  = "dc2b341acef71072eec576c6ff927b96"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="", #client_mobile_number
    from_="",#number_given by twilio
    body="Hello from Mritunjay!")

print(message.sid)
