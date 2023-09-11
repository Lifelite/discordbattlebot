from mysql_connector import Query
import random
from data.responses import initiative


class Fight:

    def __init__(self):
        self.fighterkeys = None
        q = Query()
        self.toon_list = q.get_toons()
        self.fighters_and_stats = {}
        self.bracket = []
        self.dialogue = ["WELCOME to the tournament, hope you got your characters in!"]

    def dice_roll(self, d_type):
        d_type = int(d_type)
        dice = random.randint(1, d_type)
        return dice

    def setup_toon_dict(self):
        for row in self.toon_list:
            details = [row[1],
                       row[2],
                       row[3],
                       row[4],
                       row[5]]
            self.fighters_and_stats.update({row[0]: details})
        return self.fighters_and_stats

    def fighter_list(self, t_dict):
        if len(t_dict) < 2:
            return False
        keys = list(t_dict.keys())

        random.shuffle(keys)  # Shuffles the bracket
        for toon in keys:
            self.bracket.append([toon, 0])
        return self.bracket  # Returns [["Fighter", 0]]" for each fighter

    def combat_hit(self, d1):
        if d1 == 1:
            return False
        elif d1 in range(2, 11):
            return 3
        elif d1 in range(11, 19):
            return 1
        elif d1 == 20:
            return 2

    def damage_calc(self, hp, mp):
        multiplier = self.dice_roll(10)
        attack = mp / 10
        if multiplier == 10:
            return False
        hp -= attack * multiplier
        return hp

    def f_battle(self, f1, f2, name1, name2):
        self.dialogue.append(f"IT'S TIME FOR BATTLE")
        self.dialogue.append(f"First we have {name1} the {f1[4]}")
        self.dialogue.append(f"They will fight {name2} the {f2[4]}")
        self.dialogue.append(f"************BEGIN************")

        hp1 = int(f1[1])
        hp2 = int(f2[1])
        mp1 = int(f1[2])
        mp2 = int(f2[2])
        sp1 = f1[3]
        sp2 = f2[3]
        wep1 = f1[0]
        wep2 = f2[0]
        bout = 1
        while True:
            if bout % 2 == 0:
                hp = hp2
                mp = mp1
                sp = sp1
                wep = wep1
                self.dialogue.append(f"{name1} attacks!")
            else:
                hp = hp1
                mp = mp2
                sp = sp2
                wep = wep2
                self.dialogue.append(f"{name2} attacks!")
            hitmiss = self.dice_roll(20)
            hit_result = self.combat_hit(hitmiss)
            damaged_hp = self.damage_calc(hp, mp)
            if not hit_result:
                self.dialogue.append("They somehow fumbled so badly they HEALED their opponent for 10 hp!")
                hp += 10
                bout += 1
                continue
            elif hit_result == 3:
                self.dialogue.append("Missed!")
                bout += 1
                continue
            elif hit_result == 2 or damaged_hp is False:
                self.dialogue.append(f"They use their special move, {sp}!!!  It hits for {mp} damage")
                hp = hp - mp
            else:
                self.dialogue.append(f"They strike with their {wep} for {str(hp - damaged_hp)}")
                hp = damaged_hp
            if bout % 2 == 0:
                hp2 = hp
            else:
                hp1 = hp
            if hp1 <= 0 or hp2 <= 0:
                break
            bout += 1
        willhit = self.dice_roll(2)
        if hp1 > hp2:
            if bout < 3:
                willhit = 2
            self.dialogue.append(f"{name2} near death, in a last ditch effort, uses their special move {sp2}!!!")
            if willhit == 1:
                self.dialogue.append(f"AND IT MISSED! Good attempt by {name2}, but {name1} claims victory!")
                return name1
            if mp2 > hp1 and willhit == 2:
                self.dialogue.append(f"....AND IT HITS, KILLING {name1}!  {name2}, won!!!")
                return name2
            else:
                self.dialogue.append(
                    f"It hits {name1}, but doesn't finish them!  They finish off {name2} and claim victory!")
                return name1
        elif hp2 > hp1:
            if bout < 2:
                willhit = 2
            self.dialogue.append(f"{name1} near death, in a last ditch effort, uses their special move {sp1}!!!")
            if willhit == 1:
                self.dialogue.append(f"AND IT MISSED! Good attempt by {name1}, but {name2} claims victory!")
                return name2
            if mp1 > hp2 and willhit == 2:
                self.dialogue.append(f"....AND IT HITS, KILLING {name2}!  {name1}, won!!!")
                return name2
            else:
                self.dialogue.append(
                    f"It hits {name2}, but doesn't finish them!  They finish off {name1} and claim victory!")
                return name2

    def fight_round_bracket(self):
        self.fighters_and_stats = self.setup_toon_dict()
        self.bracket = self.fighter_list(self.fighters_and_stats)
        if not self.bracket:
            return False
        # if len(self.bracket) % 2 != 0:
        #     self.bracket[0][1] += 1
        f_round = 1

        while True:
            self.dialogue.append(f"Round {f_round} in this tournament is starting!")
            matches = []
            for toon in self.bracket:
                # if toon[1] == f_round:
                #     continue
                # else:
                matches.append(toon)  # Makes a temporary list with fighters for this round
            # if len(matches) <= 1:
            #     break
            # Picks the first two fighters, then gets their stats from the dictionary
            while True:
                if len(matches) == 0:
                    break
                name1 = matches[0][0]
                name2 = matches[1][0]
                player1_rounds = matches[0][1]
                player2_rounds = matches[1][1]
                fighter1 = self.fighters_and_stats[name1]
                fighter2 = self.fighters_and_stats[name2]
                if initiative.index(fighter1[4]) <= initiative.index(fighter2[4]):
                    winner = self.f_battle(fighter1, fighter2, name1, name2)
                else:
                    winner = self.f_battle(fighter2, fighter1, name2, name1)
                if winner == name1:
                    loser = matches[1]
                    matches.pop(1)
                    matches.pop(0)
                    self.bracket.remove(loser)
                    for name in self.bracket:
                        if name[0] == name1:
                            name[1] += 1

                else:
                    loser = matches[0]
                    matches.pop(1)
                    matches.pop(0)
                    self.bracket.remove(loser)
                    for name in self.bracket:
                        if name[0] == name1:
                            name[1] += 1
                if len(matches) == 1:
                    matches[0][1] += 1
                    break

            f_round += 1
            if len(self.bracket) == 1:
                self.dialogue.append(
                    f"We have a CHAMPION!!!  May the legend of {self.bracket[0][0]} live on in history!")
                return self.dialogue
