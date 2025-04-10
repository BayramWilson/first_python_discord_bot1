# This example requires the 'message_content' intentf
from dotenv import load_dotenv
import os
import discord
load_dotenv()
import requests
from bs4 import BeautifulSoup as bs


URL = 'https://tarnkappe.info/newsticker'
req = requests.get(URL)
soup = bs(req.text, 'html.parser')
section = soup.find('section')
if section:
    first_ul = section.find('ul')
    first_link = first_ul.find('a')

    if first_link:
        title = first_link.text.strip()
        link = first_link['href']

token = os.getenv("TOKEN")


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ping'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('!Hallo'):
        await message.channel.send('Hallo Leute ich poste hier nur die aktuellen Tech News mithilfe,' \
        'einiger API´s!')
    if message.content.startswith('!News'):
        await message.channel.send(f"📰 {title}\n🔗 {link}")
client.run(token)
