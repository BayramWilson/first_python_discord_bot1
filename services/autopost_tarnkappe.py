"""
This script checks hourly if tarnkappe.info has a new post
and triggers a Discord message if so.
"""

import os
import asyncio
from datetime import datetime
from scrapes.tarnkappen_scraper import fetch_latest_news_title, fetch_latest_news_link

channel_id = int(os.getenv("NEWS_CHANNEL_ID"))
last_title = None  # Merkt sich den letzten Titel zum Vergleich

async def start_news_loop(client):
    global last_title

    # manuell definierte Stundenliste im ursprünglichen Format
    hours = [
        "00:02", "01:02", "02:02", "03:02", "04:02", "05:02",
        "06:02", "07:02", "08:02", "09:02", "10:02", "11:02",
        "12:02", "13:02", "14:02", "15:02", "16:02", "17:02",
        "18:02", "19:02", "20:02", "21:02", "22:02", "23:02"
    ]

    await client.wait_until_ready()

    while not client.is_closed():
        now = datetime.now().strftime("%H:%M")

        if now in hours:
            title = fetch_latest_news_title()
            link = fetch_latest_news_link()

            if title and title != last_title:
                last_title = title
                channel = client.get_channel(channel_id)
                if channel:
                    await channel.send(f"📰 {title}\n🔗 {link}")
                else:
                    print("❌ Channel not found or bot has no access.")
            else:
                print("🔁 Kein neuer Beitrag oder Titel leer.")

        await asyncio.sleep(60)
