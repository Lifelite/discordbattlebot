import discord
from dotenv import load_dotenv, find_dotenv
import os

# import data_files.formdata
# from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/build'):
        await message.channel.send('Hello!')


# @client.event
# async def test_command(message):
#     if

load_dotenv(find_dotenv())
token = os.environ.get("DISCORD_CLIENT")
client.run(str(token))

