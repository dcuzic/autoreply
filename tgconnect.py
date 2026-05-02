import os
from dotenv import load_dotenv
from telethon import TelegramClient

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("session", api_id, api_hash)

client.start()
print("Client started")

# test tg connection
async def test_connection():
    me = await client.get_me()
    print(f"Username: {me.username}, ID: {me.id}")

with client:
    client.loop.run_until_complete(test_connection())
