import os

import discord

from discord.ext import commands

from dotenv import load_dotenv, find_dotenv

from data import responses
from ui import BuildModal


# intents = discord.Intents.default()
# intents.message_content = True
# client = discord.Client(intents=intents)
# bot = commands.Bot(command_prefix='/', intents=intents)


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(command_prefix='$', intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')


# @bot.command(name='help')
# async def _help(ctx):
#     await ctx.send(responses.response_dict["help"])

bot = Bot()


@bot.command()
async def build(ctx):
    # await ctx.send(responses.response_dict["class_build"])
    view = BuildModal()
    await ctx.send('Build your Character', view=view)
    await ctx.send(f" {discord.Interaction.user} Submitted a character!")


@bot.command(name='view')
async def _view(ctx):
    await ctx.send("TODO:ADDVIEW")


load_dotenv(find_dotenv())
token = os.environ.get("DISCORD_CLIENT")
bot.run(str(token))
