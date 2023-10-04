from urllib.parse import urlparse

from dotenv import dotenv_values

from telethon import TelegramClient, events

config = dotenv_values(".env")

api_id = config["api_id"]
api_hash = config["api_hash"]
bot_token = config["bot_token"]

if (api_id is None or api_hash is None or bot_token is None):
    raise Exception("Invalid .env configuration")

api_id = int(api_id)

client = TelegramClient('client', api_id, api_hash)
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

url_regex = r'https?://\S+|www\.\S+'

@client.on(events.NewMessage(incoming=False, outgoing=True, forwards=False, pattern=url_regex))
async def edit_message_url(event):
    replacements = {
        'twitter.com': 'vxtwitter.com',
        'x.com': 'vxtwitter.com',
        'furaffinity.net': 'vxfuraffinity.net',
    }

    parsed_url = urlparse(event.raw_text)

    for old_url, new_url in replacements.items():
        if old_url == parsed_url.netloc:
            parsed_url = parsed_url._replace(netloc=new_url)
            parsed_url = parsed_url._replace(query='')

            await client.edit_message(
                entity=await event.get_chat(),
                message=event.message,
                text=parsed_url.geturl(),
                link_preview=True
            )
            break

def start():
    client.start()
    bot.start()
    print("🚀 App started!")
    client.run_until_disconnected()

start()
