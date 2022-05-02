import discord
import os
from dotenv import load_dotenv

load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        
        await message.add_reaction('🐿️')

intents = discord.Intents.default()

client = MyClient()
client.run(os.getenv('BOT_TOKEN'))