import discord.ui
from discord import ui


class Toon(ui.Modal, title="Build your Character"):

    def __init__(self):
        super().__init__()
        self.sp_move = discord.ui.TextInput(
            label='Name Your Special Move',
            placeholder='Falcon Punch...'
        )
        self.name = discord.ui.TextInput(
            label='Character Name',
            placeholder='Name your character....'
        )

