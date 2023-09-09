import discord
from discord import ui
from functions import Functions
from data.toon_classes import *


class TextModal(discord.ui.Modal, title="Build your Character"):

    def __init__(self, c_name):
        super().__init__()
        self.c_name = c_name

    name = ui.TextInput(
        label='Character Name',
        placeholder='Name your character....'
    )

    sp_move = ui.TextInput(
        label='Name Your Special Move',
        placeholder='Falcon Punch...'
    )

    async def on_submit(self, interaction: discord.Interaction):
        funct = Functions(self.name, self.sp_move, self.c_name)
        funct.toon_upload({interaction.user.name})
        await interaction.response.send_message(f"Thanks for your submission, {interaction.user.name}")


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


class BuildModal(discord.ui.View):
    @discord.ui.select(
        options=[
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
                                 description="Either overpowered or nerfed to hell...no inbetween.",
                                 value="Shaman"),

            discord.SelectOption(label='Warlock',
                                 description="See Mages are dumb, just do a deal with the devil and get a similar result, duh.",
                                 value="Warlock"),

            discord.SelectOption(label='Warrior',
                                 description="Enjoys the simple things in life.  Involves crushing skulls.",
                                 value="Warrior")

        ],
        placeholder='Choose your class...',
        min_values=1,
        max_values=1
    )
    async def select_callback(self, interaction: discord.Interaction, select):
        await interaction.response.send_modal(TextModal(select.values[0]))
        await interaction.edit_original_response(view=None)

