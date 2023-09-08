class Toon:

    def __init__(self, name, t_class, hp, mp, weapon, sp_move):
        self.name = name
        self.t_class = t_class
        self.hp = hp
        self.mp = mp
        self.weapon = weapon
        self.sp_move = sp_move

    def build(self):
        while True:
            name = input("What do you want to name your character?\n\n> ")
            sp_question = input("Would you like to name your special move?\n\n> ")
            if "y" in sp_question.lower():
                sp_move = input("Awesome, what do you want to name the move? (Please keep it somewhat family "
                                "friendly)\n\n> ")
                print(f"Your {self.t_class} is name {c_name}, with the special move: {sp_move}\n\n")
                confirm_toon = input('Finalize your Character? (y / n) > ')
                if "y" in confirm_toon.lower():
                    self.name = name
                    self.sp_move = sp_move
                    print(self.name, self.t_class, self.hp, self.mp, self.weapon, self.sp_move)
                else:
                    continue





class Druid(Toon):

    def __init__(self, name, sp_move="Bear Slam", hp=100, mp=100, weapon="Wolf Claws", t_class="Druid"):
        super().__init__(name, t_class, hp, mp, weapon, sp_move)



class Ranger(Toon):

    def __init__(self, name, sp_move="Explosive Arrow", hp=90, mp=110, weapon="Bow", t_class="Ranger"):
        super().__init__(name, t_class, hp, mp, weapon, sp_move)


class Mage(Toon):

    def __init__(self, name, sp_move="Fireball", hp=10, mp=190, weapon="Magic Staff", t_class="Mage"):
        super().__init__(name, t_class, hp, mp, weapon, sp_move)


class Paladin(Toon):

    def __init__(self, name, sp_move="Holy Slash", hp=160, mp=40, weapon="Sword & Shield", t_class="Paladin"):
        super().__init__(name, t_class, hp, mp, weapon, sp_move)


class Priest(Toon):

    def __init__(self, name, sp_move="Smite", hp=20, mp=180, weapon="Holy Scepter", t_class="Priest"):
        super().__init__(name, t_class, hp, mp, weapon, sp_move)


class Rogue(Toon):

    def __init__(self, name, sp_move="Blade Tornado", hp=80, mp=120, weapon="Daggers", t_class="Rogue"):
        super().__init__(name, t_class, hp, mp, weapon, sp_move)


class Shaman(Toon):

    def __init__(self, name, sp_move="Elemental Earthquake", hp=110, mp=90, weapon="Totem", t_class="Shaman"):
        super().__init__(name, t_class, hp, mp, weapon, sp_move)


class Warlock(Toon):

    def __init__(self, name, sp_move="Demonic Lightning", hp=30, mp=170, weapon="Cursed Sword", t_class="Warlock"):
        super().__init__(name, t_class, hp, mp, weapon, sp_move)


class Warrior(Toon):

    def __init__(self, name, sp_move="Cleave", hp=130, mp=70, weapon="Warhammer", t_class="Warrior"):
        super().__init__(name, t_class, hp, mp, weapon, sp_move)