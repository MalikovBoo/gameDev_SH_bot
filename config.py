import os
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("TG_API_KEY")
api_key = os.getenv("GPT_API_KEY")
