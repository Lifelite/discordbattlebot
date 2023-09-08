import discord
from functions import Functions
from data.toon_classes import *


# class CharacterInputs(ui.Modal, title=f"Build your Character"):
#
#     def __init__(self, c_type):
#         super().__init__()
#         self.c_type = c_type


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

    def __init__(self):
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

    async def callback(self, response: discord.Interaction):
        thing = assignType(self.values[0])
        await response.response.send_modal(thing)
        self.disabled = True
        await response.edit_original_response(
            view=self.view
        )


class BuildModal(discord.ui.View):

    def __init__(self):
        super().__init__()
        self.add_item(Dropdown())
    # async def on_submit(self, interaction: discord.Interaction):
    #     # await interaction.response.reply(f'Welcome your challenger, {self.c_name} has joined the Tournament!')
    #     t_class = Dropdown.values
    #     user = discord.Interaction.user
    #
    #     f = Functions(self.c_name, self.sp_move, t_class)
    #     f.toon_upload(user)
