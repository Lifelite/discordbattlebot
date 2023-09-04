import discord
from interactions import Bot


class InputHelpers(Bot):

    def __init__(self):

        super().__init__()

    def message_validate(self, vtype, u_input):
        if vtype == "int":
            try:
                number = int(u_input)
                return number
            except TypeError:
                return False

        if vtype == "str":
            try:
                u_string = str(u_input)
                return u_string
            except TypeError:
                return False

# class View(discord.ui.View):
#
#     @discord.ui.select(cls=ChannelSelect, channel_types=[discord.ChannelType.text])
#     async def select_channels(self, interaction: discord.Interaction, select: ChannelSelect):
#         return await interaction.response.send_message(f'You selected {select.values[0].mention}')
