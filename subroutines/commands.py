import os
import time

import discord
from discord import ui
from discord.ext import commands
from datetime import datetime

from dotenv import load_dotenv, find_dotenv

from subroutines.fight import Fight
from subroutines.ui import BuildModal, ViewButton, DeleteButton, DeleteALLButton
from mysql_connector import *


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)


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


@bot.command()
async def blank(ctx):
    view = DeleteALLButton()
    await ctx.send(view=view)


@bot.command()
async def fight(ctx):
    f = Fight()
    f.fight_round_bracket()
    for message in f.dialogue:
        await ctx.send(message)
        time.sleep(3)


load_dotenv(find_dotenv())
token = os.environ.get("DISCORD_CLIENT")
bot.run(str(token))
