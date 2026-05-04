import os
from dotenv import load_dotenv
from telethon import TelegramClient, events
import asyncio
from database import db_conn

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("session", api_id, api_hash)

async def send_db(incoming, sender):
    conn = db_conn()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO incoming (incoming, sender) VALUES (?, ?)", (incoming, sender))

    conn.commit()
    conn.close()


@client.on(events.NewMessage)
async def handler(event):


    if event.voice:
        incoming = "🎤 Voice message"

    sender = await event.get_sender()
    id = sender.id
    
    print(sender.first_name, sender.last_name + ":", incoming)
    print(sender.username)
    print("ID:", sender.id)
    print("Recording to the database...")
    

async def main():
    await client.start()
    print("Client started")

    me = await client.get_me()
    print(f"Username:{me.username}, ID: {me.id}")

    print("Client running ...")

    await client.run_until_disconnected()


asyncio.run(main())



