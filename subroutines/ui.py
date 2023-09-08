import discord
from discord import ui

from functions import Functions
from data.toon_classes import *


class TextModal(ui.Modal, title="Build your Character"):

    def __init__(self, c_class):
        super().__init__()
        self.sp_move = ui.TextInput(
            label='Name Your Special Move',
            placeholder='Falcon Punch...'
        )
        self.name = ui.TextInput(
            label='Character Name',
            placeholder='Name your character....'
        )
        self.c_class = c_class

    async def on_submit(self, interaction: discord.Interaction):
        funct = Functions(self.name, self.sp_move, self.c_class)
        funct.toon_upload({interaction.user})


def assignType(number):
    classes = {
        "Druid": Druid,
        "Ranger": Ranger,
        "Mage": Mage,
        "Paladin": Paladin,
        "Priest": Priest,
        "Rogue": Rogue,
        "Shaman": Shaman,
        "Warlock": Warlock,
        "Warrior": Warrior,
    }
    return classes[number]()


class Dropdown(discord.ui.Select):

    def __init__(self, ctx):
        options = [
            discord.SelectOption(label='Druid',
                                 description="The class of nature...and furry..-er.. I mean fury", value="Druid"),

            discord.SelectOption(label='Ranger',
                                 description="Bear Gryllz ain't got shit on you", value="Ranger"),

            discord.SelectOption(label='Mage',
                                 description="lol, Fireball goes brrrrrrrrrr.  Don't touch me.", value="Mage"),

            discord.SelectOption(label='Paladin',
                                 description="Sword and board, with blessing from whatever deity.  Probably a basic bitch.",
                                 value="Paladin"),

            discord.SelectOption(label='Priest',
                                 description="Healers, gotta love them. Just a bad day away from cult leader.",
                                 value="Priest"),

            discord.SelectOption(label='Rogue',
                                 description="Let me guess, you're chaotic neutral.", value="Rogue"),

            discord.SelectOption(label='Shaman',
                                 description="Either overpowered or nerfed to hell...no inbetween.", value="Shaman"),

            discord.SelectOption(label='Warlock',
                                 description="See Mages are dumb, just do a deal with the devil and get a similar result, duh.",
                                 value="Warlock"),

            discord.SelectOption(label='Warrior',
                                 description="Enjoys the simple things in life.  Involves crushing skulls.",
                                 value="Warrior")

        ]

        super().__init__(placeholder='Choose your class...', min_values=1, max_values=1, options=options)
        self.ctx = ctx

    async def callback(self, response: discord.InteractionResponse):
        thing = TextModal(self.values[0])
        await self.ctx.response.send_modal(thing)
        self.disabled = True
        await response.edit_message(
            view=self.view
        )


class BuildModal(discord.ui.View):

    def __init__(self, ctx):
        super().__init__()
        self.add_item(Dropdown(ctx))
