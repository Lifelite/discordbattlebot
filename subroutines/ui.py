import discord
from discord.ui import ChannelSelect
from data import responses
import discord.ui as ui
from functions import Functions


class Dropdown(discord.ui.Select):

    def __init__(self):
        options = [
            discord.SelectOption(label='Druid',
                                 description="The class of nature...and furry..-er.. I mean fury"),

            discord.SelectOption(label='Ranger',
                                 description="Bear Gryllz ain't got shit on you"),

            discord.SelectOption(label='Mage',
                                 description="lol, Fireball goes brrrrrrrrrr.  Don't touch me."),

            discord.SelectOption(label='Paladin',
                                 description="Sword and board, with blessing from whatever deity.  Probably a basic bitch."),

            discord.SelectOption(label='Priest',
                                 description="Healers, gotta love them. Just a bad day away from cult leader."),

            discord.SelectOption(label='Rogue',
                                 description="Let me guess, you're chaotic neutral."),

            discord.SelectOption(label='Shaman',
                                 description="Either overpowered or nerfed to hell...no inbetween."),

            discord.SelectOption(label='Warlock',
                                 description="See Mages are dumb, just do a deal with the devil and get a similar result, duh."),

            discord.SelectOption(label='Warrior',
                                 description="Enjoys the simple things in life.  Involves crushing skulls.")

        ]

        super().__init__(placeholder='Choose your class...', min_values=1, max_values=1, options=options)


# class DropdownView(discord.ui.View):
# def __init__(self):
# super().__init__()

# self.add_item(Dropdown())
# class CharName(discord.ui.TextInput):


class BuildModal(discord.ui.Modal, title='Character Builder'):

    def __init__(self):
        super().__init__(title="Character Builder")
        self.select = Dropdown()

        self.c_name = ui.TextInput(label="Character Name:", placeholder="Name your character...", required=True)
        self.sp_move = ui.TextInput(label="Special Move:", placeholder="Want to add a special move?",required=False)
        self.add_item(item=self.select)
        self.add_item(item=self.c_name)
        self.add_item(item=self.sp_move)

    async def on_submit(self, interaction: discord.Interaction):
        # await interaction.response.reply(f'Welcome your challenger, {self.c_name} has joined the Tournament!')
        t_class = Dropdown.values
        user = discord.Interaction.user

        f = Functions(self.c_name, self.sp_move, t_class)
        f.toon_upload(user)
