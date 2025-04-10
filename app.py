import os
import discord
import requests
from bs4 import BeautifulSoup as bs

# News scrapen
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


# Token aus Umgebungsvariable
token = os.getenv("TOKEN")

if not token:
    print("TOKEN nicht gefunden")
    exit()

# Bot konfigurieren
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot ist online als {client.user}')

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
        await message.channel.send(f"📰 {title}\n🔗 {link}")

# Bot starten
client.run(token)
