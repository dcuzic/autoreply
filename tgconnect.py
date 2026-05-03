import os
from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("session", api_id, api_hash)

async def main():
    client.start()
    print("Client started")

    me = await client.get_me()
    print(f"Username:{me.username}, ID: {me.id}")

with client:
    client.loop.run_until_complete(main())

@client.on(events.NewMessage)
async def message(event):
    await event.