import discord

from data.toon_classes import *
from mysql_connector import *

MY_GUILD = discord.Object(id=360611536672129025)
#
#
# class InputHelpers(Bot):
#
#     def __init__(self):
#
#         super().__init__()
#
#     def message_validate(self, vtype, u_input):
#         if vtype == "int":
#             try:
#                 number = int(u_input)
#                 return number
#             except TypeError:
#                 return False
#
#         if vtype == "str":
#             try:
#                 u_string = str(u_input)
#                 return u_string
#             except TypeError:
#                 return False

# class View(discord.ui.View):
#
#     @discord.ui.select(cls=ChannelSelect, channel_types=[discord.ChannelType.text])
#     async def select_channels(self, interaction: discord.Interaction, select: ChannelSelect):
#         return await interaction.response.send_message(f'You selected {select.values[0].mention}')

class Functions:

    def __init__(self, c_name, sp_move, c_class):
        self.c_name = c_name
        self.sp_move = sp_move
        self.c_class = c_class

    def toon_upload(self, t_user):
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
        aToon = classes[self.c_class](self.c_name, self.sp_move)

        q = Query()
        q.commit_toon(aToon.name, aToon.weapon, aToon.hp, aToon.mp, aToon.sp_move, aToon.t_class, t_user)

    def get_toon_list(self):
        q = Query()
        q.get_toons()
