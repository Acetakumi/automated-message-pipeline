import os
from datetime import datetime
from generate_quote import get_romantic_quote
from config import Config
from twilio.rest import Client

quote = get_romantic_quote()

def update_readme(quote):
    today = datetime.now().strftime("%Y-%m-%d")

    new_entry = f"\n### {today}\n> {quote}\n"

    with open("README.md", "a", encoding="utf-8") as f:
        f.write(new_entry)

update_readme(quote)

config = Config()
account_sid = config.account_sid
auth_token = config.auth_token
from_number = config.from_number
to_number = config.to_number
message = config.message

client = Client(account_sid, auth_token)

message = client.messages.create(
    body=f"{quote} \n{message}",
    from_=from_number,
    to=to_number,
)

print("Message SID:", message.sid)
print(message.body)