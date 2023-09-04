import discord
from discord.ui import ChannelSelect
from data import responses


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

    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        # selected options. We only want the first one.
        await interaction.response.send_message(f'Your chosen class is: {self.values[0]}')
        return self.values[0]


class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(Dropdown())



# https://github.com/Rapptz/discord.py/blob/94655cd804d01bef8f514412d20909cedb1371da/examples/views/dropdown.py

# https://github.com/Rapptz/discord.py/blob/94655cd804d01bef8f514412d20909cedb1371da/examples/modals/basic.py