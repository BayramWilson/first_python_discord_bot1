import os
import discord
import datetime
from discord.ext import commands, tasks
from scrapes.tarnkappen_scraper import fetch_latest_news_title, fetch_latest_news_link
from services.autopost_tarnkappe import start_news_loop
from services.daily_message import gptCall
token = os.getenv("TOKEN")
if not token:
    print("TOKEN nicht gefunden")
    exit()

#Zeit abfragen
utc = datetime.timezone.utc

# If no tzinfo is given then UTC is assumed.
# german time 8:30
time = datetime.time(hour=6, minute=30, tzinfo=utc)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@tasks.loop(time=time)
async def send_daily_motivation():
    message = gptCall()
    channel_id = int(os.getenv("MINDSET_CHANNEL_ID"))
    channel = client.get_channel(channel_id)
    if channel:
        await channel.send(message)


@client.event
async def on_ready():
    print(f' Bot ist online als {client.user}')
    client.loop.create_task(start_news_loop(client))
    send_daily_motivation.start()
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ping'):
        await message.channel.send('Hello!')

    elif message.content.startswith('!Hallo'):
        await message.channel.send('Hallo Leute! Ich poste hier aktuelle Tech-News mithilfe einiger APIs!')

    elif message.content.startswith('!help'):
        await message.channel.send('Verfügbare Befehle: `!News`, `!Hallo`, `!ping`')

    elif message.content.startswith('!News'):
        await message.channel.send(f"📰 {fetch_latest_news_title()}\n🔗 {fetch_latest_news_link()}")
    elif message.content.startswith('!Motivation'):
        await message.channel.send(gptCall())
client.run(token)
