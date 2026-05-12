# 📨 Autoreply

A Telegram auto-reply tool that automatically responds to incoming messages during your busy hours.

## What it does

- Monitors your Telegram for incoming messages
- Automatically replies to whitelisted contacts during your busy time window
- Sends one reply per person per day (no spam)
- Prints a daily report at a time you choose
- Logs all incoming messages to a local database

## Requirements

- Python 3.10+
- A Telegram account
- Telegram API credentials (free, see setup below)

## Installation

```bash
pip install telethon pynput python-dotenv
```

## First run

```bash
python main.py
```

On first launch the app will walk you through setup step by step:

1. **API credentials** — enter your Telegram `API_ID` and `API_HASH` (saved to `.env` automatically)
2. **Busy interval** — the time window during which auto-replies are sent (e.g. `09:00` to `17:00`, supports overnight intervals like `22:00` to `01:00`)
3. **Whitelist** — names of contacts you want to auto-reply to
4. **Report time** — when to print the daily summary of received messages
5. **Responses** — 3 reply messages (one is picked at random each time)

After setup, the Telegram client starts and runs in the background.

## Getting API credentials

1. Go to [my.telegram.org](https://my.telegram.org)
2. Log in with your phone number
3. Go to **API development tools**
4. Create an app — copy the `api_id` and `api_hash`

## Usage

```bash
python main.py
```

Press `` ` `` (backtick) at any time to exit.

## File structure

```
autoreply/
├── main.py          # entry point, setup flow
├── tgconnect.py     # telegram client, message handler
├── database.py      # database helpers
├── .env             # api credentials (auto-created)
└── session.session  # telegram session (auto-created)
```

## Building an executable

```bash
pip install pyinstaller
pyinstaller --onefile --name "autoreply" main.py
```

The `.exe` will be in the `dist/` folder. On first launch it will ask for API credentials and create all necessary files automatically.

## Notes

- The app will only auto-reply while the current time is within your busy interval
- Each contact on the whitelist receives at most one auto-reply per day
- The session file keeps you logged in between launches — do not delete it unless you want to re-authenticate
