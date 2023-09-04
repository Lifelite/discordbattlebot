import discord
from interactions import Bot

class InputHelpers(Bot):

    def __init__(self):

        super().__init__()

    def message_validate(self, vtype, u_input):
        if vtype is "int":
            try:
                number = int(u_input)
                return number
            except TypeError:
                return False

        if vtype is "str":
            try:
                u_string = str(u_input)
                return u_string
            except TypeError:
                return False


#A discord battle bot that allows users to build characters and have them battle in a tournament style format.