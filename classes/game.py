import random
from .magic import Spell
import pprint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN ='\033[32m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk -10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]
        self.name = name


    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n" + "        " + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "    ACTIONS" + bcolors.ENDC)
        for item in self.actions:
            print("    " + str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    MAGIC" + bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1

        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "    ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print ("        " + str(i) + ".", item["item"].name + ":", item["item"].description, " (x" + str(item["quantity"]) + ")")
            i += 1


    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "    TARGET:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print ("        " + str(i) + ".", enemy.name)
                i += 1
        choice = int(input("    Choose traget:"))- 1
        return choice

    def get_enemy_stats(self):
        hp_bar = ""
        hp_bar += "║" * int((self.hp / self.maxhp) * 50)
        hp_string = f"{self.hp}/{self.maxhp}"
        print(f'{" ":40}{"_" * 50}')
        print(f"{self.name:30}" + f"{hp_string:9}|" + bcolors.FAIL + f"{hp_bar:50}" + bcolors.ENDC + "|")

    def get_stats(self):
        hp_bar = ""
        mp_bar = ""
        # Int to use multiplication to fill the string
        hp_bar += "║" * int((self.hp / self.maxhp) * 25)
        mp_bar += "║" * int((self.mp / self.maxmp) * 10)
        hp_string = f"{self.hp}/{self.maxhp}"
        mp_string = f"{self.mp}/{self.maxmp}"
        print(f'{" ":40}{"_" * 25}{" ":10}{"_" * 10}')
        print(f"{self.name:30}" + f"{hp_string:9}|" + bcolors.OKGREEN + f"{hp_bar:<25}" + bcolors.ENDC + "| " + f"{mp_string:7}|" + bcolors.OKBLUE + f"{mp_bar:<10}" + bcolors.ENDC + "|")



    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()


        pct = self.hp / self.maxhp * 100

        if self.mp < spell.cost or spell.type == "white" and pct > 50 :
            self.choose_enemy_spell()
        else:
            return spell, magic_dmg