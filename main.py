
import logging
import os
import discord

from dotenv import load_dotenv

load_dotenv()

class SquirrelClient(discord.Client):
    async def on_ready(self):
        logging.info(f'Bot is ready as user {self.user}')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        
        await message.add_reaction('🐿️')

intents = discord.Intents.default()

client = SquirrelClient()
client.run(os.getenv('BOT_TOKEN'))