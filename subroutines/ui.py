import discord
from discord.ui import ChannelSelect
from data import responses

class Dropdown(discord.ui.Select):

    def __init__(self):

        options = [
            discord.SelectOption(label='Druid', description="A person of nature...and fury")
        ]


# https://github.com/Rapptz/discord.py/blob/94655cd804d01bef8f514412d20909cedb1371da/examples/views/dropdown.py