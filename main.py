import discord
from discord import ui
from dotenv import load_dotenv, find_dotenv
import os
# from subroutines import functions
from subroutines import interactions

# import data_files.formdata
# from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.create_private_threads = True


client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user = message.author

    h = interactions.Help(client, message, user)

    if message.content.startswith('/help'):
        await h.help_command()


# @client.event
# async def test_command(message):
#     if

load_dotenv(find_dotenv())
token = os.environ.get("DISCORD_CLIENT")
client.run(str(token))
