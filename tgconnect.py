import os
import asyncio
import datetime
import random
from telethon import TelegramClient, events
from pynput import keyboard
from dotenv import load_dotenv
from database import db_conn


load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("session", api_id, api_hash)

async def send_db(date, incoming, sender, sender_id):
    conn = db_conn()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO incoming (date, incoming_message, sender, sender_id) VALUES (?, ?, ?, ?)", (date, incoming, sender, sender_id))

    conn.commit()
    conn.close()

def clear_previous_incoming():
    conn = db_conn()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM incoming")

    conn.commit()
    conn.close()

def response():
    conn = db_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages WHERE message_id = 1")
    response1 = cursor.fetchone()

    cursor.execute("SELECT * FROM messages WHERE message_id = 2")
    response2 = cursor.fetchone()    

    cursor.execute("SELECT * FROM messages WHERE message_id = 3")
    response3 = cursor.fetchone()

    responses_list = [response1, response2, response3]
    
    response_choice = random.choice(responses_list)

    return response_choice["message"]

def replied_today(id):
    conn = db_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT sender_id FROM incoming")
    already_replied_id_list = [
        item[0] for item in cursor.fetchall()]

    if id in already_replied_id_list:
        return True
    else:
        return False


def whitelist_check(first_name, last_name):
    conn = db_conn()
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM whitelist WHERE name = ?", 
                   (f"{first_name, last_name}",)
                   )
    
    return cursor.fetchone is not None


@client.on(events.NewMessage)
async def handler(event):
    
    sender = await event.get_sender()
    id = sender.id

    recieved_at = event.date.astimezone()
    format_code = "%d/%m/%Y %H:%M"

    parsed_date = recieved_at.strftime(format_code)

    if event.raw_text:
        incoming = event.raw_text

    elif event.voice:
        incoming = "🎤 Voice message"

    elif event.video_note:
        incoming = "📸 Video message"

    elif event.video:
        incoming = "📸 Video"
        
    elif event.photo:
        incoming = "🖼️ Photo"

    elif event.geo:
        incoming = "📌 Location"

    elif event.sticker:
        incoming = "Sticker"
    
    elif event.document:
        incoming = f"📄 {event.file.name}"

    else:
        incoming = "Unsupported or Empty message"

    print(parsed_date)
    print(sender.first_name, sender.last_name + ":", incoming)

    if replied_today(id) == True:
        print("Already replied, so not replying")
        pass

    if replied_today(id) == False:

        if whitelist_check(sender.first_name, sender.last_name) == True:

            print("Replying...")

            response_result = response()
            await event.reply(response_result)

            print(f"Replied with: {response_result}")
        else:
            print("Person is not in whitelist, not replying.")

    print("Recording to the database...")
    sender_full_name = sender.first_name + " " + sender.last_name

    await send_db(parsed_date, incoming, sender_full_name, id)

    print("Recorded.")


def stop_listener(client, loop):

    def on_press(key):

        try:
            if key.char == "`":
                print("Exiting...")
                loop.call_soon_threadsafe(lambda: client.disconnect())
                listener.stop()
                return False
        except AttributeError:
            pass
        
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

async def main():
    await client.start()
    loop = asyncio.get_running_loop()
    print("Client started")

    print("Clearing previous data...")
    clear_previous_incoming()
    print("Cleared")

    me = await client.get_me()
    print(f"Username:{me.username}, ID: {me.id}")

    print("Client running ...")

    print('Press "`" to exit')
    stop_listener(client, loop)

    await client.run_until_disconnected()

asyncio.run(main())