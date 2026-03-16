import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    account_sid: str = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token: str = os.environ.get("TWILIO_AUTH_TOKEN") 
    from_number: str = os.environ.get("TWILIO_FROM_NUMBER")
    to_number: str = os.environ.get("TO_NUMBER")
    message: str = os.environ.get("MESSAGE")
    ninja_api_key: str = os.environ.get("NINJA_API_KEY")