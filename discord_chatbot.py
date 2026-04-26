import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

import chatting

class MyBot(commands.Bot):
    async def setup_hook(self):
        await self.add_cog(chatting.ChattingCog(self))

def run():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    intents = discord.Intents.default()
    intents.message_content = True
    
    bot = MyBot(command_prefix='!', intents=intents, help_command=None)

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running!')

    bot.run(TOKEN)