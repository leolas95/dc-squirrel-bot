import discord
import os
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f'Reacting to {message.content[:20]} with 🐿️')
    await message.add_reaction('🐿️')

client.run(os.getenv('BOT_TOKEN'))