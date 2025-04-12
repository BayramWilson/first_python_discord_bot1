import os
import asyncio
from datetime import datetime
from scrapes.tarnkappen_scraper import fetch_latest_news_title, fetch_latest_news_link

channel_id = int(os.getenv("NEWS_CHANNEL_ID"))
last_title = None

async def get_last_posted_title(channel):
    async for message in channel.history(limit=50):
        if message.author.bot and message.content.startswith("📰"):
            return message.content.split("\n")[0][2:].strip()
    return None

async def start_news_loop(client):
    global last_title

    hours = [
        "00:02", "01:02", "02:02", "03:02", "04:02", "05:02",
        "06:02", "07:02", "08:02", "09:02", "10:02", "11:02",
        "12:02", "13:02", "14:02", "15:02", "16:02", "17:02",
        "18:02", "19:02", "20:02", "21:02", "22:02", "23:02"
    ]

    await client.wait_until_ready()
    channel = client.get_channel(channel_id)

    if channel:
        last_title = await get_last_posted_title(channel)
        print(f"📌 Zuletzt geposteter Titel: {last_title}")
    else:
        print("❌ Channel not found.")
        return

    while not client.is_closed():
        now = datetime.now().strftime("%H:%M")

        if now in hours:
            title = fetch_latest_news_title()
            link = fetch_latest_news_link()

            if title and title != last_title:
                last_title = title
                await channel.send(f"📰 {title}\n🔗 {link}")
            else:
                print("🔁 Kein neuer Beitrag oder Titel leer.")

        await asyncio.sleep(60)
