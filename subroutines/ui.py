import discord
from discord.ext import tasks
from discord import ui, Intents
from functions import Functions
from data.toon_classes import *
from subroutines.mysql_connector import Query


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
        username = interaction.user.name
        username = str(username)
        username = username.translate({ord(i): None for i in "' {}"})
        q = Query()
        u_name = q.find_toon(username)
        if u_name is None:
            await interaction.response.send_modal(TextModal(select.values[0]))
            await interaction.edit_original_response(content="", view=None)
        else:
            await interaction.response.edit_message(content="You already have a character!", view=None)


class ViewButton(discord.ui.View):
    @discord.ui.button(label='View Your Toon!', style=discord.ButtonStyle.blurple)
    async def view(self, interaction: discord.Interaction, button: discord.ui.Button):
        username = interaction.user.name
        username = str(username)
        username = username.translate({ord(i): None for i in "' {}"})
        q = Query()
        u_name = q.find_toon(username)
        if u_name is None:
            await interaction.response.send_message("Yo!  You need to make a character first, duh!")
        else:
            message = f"""
            Class:                   {u_name[5]}
Name:                  {u_name[0]}
Weapon:              {u_name[1]}
HP:                       {u_name[2]}
MP:                      {u_name[3]}
Special move:   {u_name[4]}
            """
            await interaction.user.send(message)
            await interaction.response.edit_message(content="Character Viewed!", view=None)


class DeleteButton(discord.ui.View):
    @discord.ui.button(label='DELETE (No going back!)', style=discord.ButtonStyle.blurple)
    async def view(self, interaction: discord.Interaction, button: discord.ui.Button):
        username = interaction.user.name
        username = str(username)
        username = username.translate({ord(i): None for i in "' {}"})
        q = Query()
        u_name = q.find_toon(username)
        if u_name is None:
            await interaction.response.send_message("Yo!  You need to make a character first, duh!")
        else:
            q.kill_toon(username)
            await interaction.response.edit_message(content="Character Killed!  You heartless monster!!!", view=None)


class DeleteALLButton(discord.ui.View):
    @discord.ui.button(label='DELETE (No going back!)', style=discord.ButtonStyle.blurple)
    async def view(self, interaction: discord.Interaction, button: discord.ui.Button):
        if "173299413882634240" in interaction.user:
            q = Query()
            q.delete_everything()
            await interaction.response.edit_message(content="All characters nuked!  Savage AF!", view=None)
        else:
            interaction.response.send_message(content="Nuh uh uh!  You can't do that")

