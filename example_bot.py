# This example requires the 'message_content' intentf
from dotenv import load_dotenv
import os
import discord
load_dotenv()

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

client.run(token)
