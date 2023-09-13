import discord

from data.toon_classes import *
from mysql_connector import *

MY_GUILD = discord.Object(id=360611536672129025)


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

