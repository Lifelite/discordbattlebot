import os

import discord
from discord import ui
from discord.ext import commands
from datetime import datetime

from dotenv import load_dotenv, find_dotenv

from subroutines.ui import BuildModal, ViewButton, DeleteButton
from mysql_connector import *


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        # self.tree = app_commands.CommandTree(self)

    # async def setup_hook(self):
    #     self.tree.copy_global_to(guild=MY_GUILD)
    #     await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
client = MyClient(intents=intents)


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='$', intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')


bot = Bot()


@bot.command()
async def build(ctx):
    view = BuildModal()
    await ctx.send("Build your Character!", view=view)


@bot.command()
async def view(ctx):
    view = ViewButton()
    await ctx.send(view=view)


@bot.command()
async def remove(ctx):
    view = DeleteButton()
    await ctx.send(view=view)


load_dotenv(find_dotenv())
token = os.environ.get("DISCORD_CLIENT")
bot.run(str(token))
