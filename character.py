from ast import List
from dice import Dice

class AbilityScore:
    def __init__(self, prof = 1, str = 10, dex = 10, con = 10, int = 10, wis = 10, cha = 10):
        self.prof = prof
        self.str = str
        self.dex = dex
        self.con = con
        self.int = int
        self.wis = wis
        self.cha = cha

    def modifier(self, score):
        return int(score / 2) - 5
    
    def str_mod(self):
        return self.modifier(self.str)

    def dex_mod(self):
        return self.modifier(self.dex)
    
    def con_mod(self):
        return self.modifier(self.con)

    def int_mod(self):
        return self.modifier(self.int)

    def wis_mod(self):
        return self.modifier(self.wis)
    
    def cha_mod(self):
        return self.modifier(self.cha)

    def __repr__(self):
        return "Abilities " + str({ "proficiency": self.prof, "strength": self.str, "dexterity": self.dex,
                                    "constitution": self.con, "intelligence": self.int,
                                    "wisdom": self.wis, "charisma": self.cha}) \
            + "\nModifiers" + str({ "STR": self.str_mod(), "DEX": self.dex_mod(),
                                    "CON": self.con_mod(), "INT": self.int_mod(),
                                    "WIS": self.wis_mod(), "CHA": self.cha_mod()})

class Weapon:
    def __init__(self, attack = 0, damage = 0, roll: List = [Dice.d4]):
        self.attack = attack
        self.damage = damage if damage != 0 else attack
        self.roll = roll
    
    def __repr__(self):
        return "Weapon " + str({ "attack": self.attack, "damage": self.damage, "roll": [r.__name__ for r in self.roll]})


class Damage:
    def __init__(self, attack: int = 0, damage: int = 0):
        self.attack = attack
        self.damage = damage

    def __repr__(self):
        return "Damage " + str({ "attack roll": self.attack, "attack damage": self.damage})
    
    def damage(hits: List = [], ac: int = 10):
        success = [h for h in hits if h.attack >= ac]
        print(len(success), "/", len(hits), "hits for", sum([h.damage for h in success]), "damage on creature with ac", ac)
        return sum([h.damage for h in success])


class Character:
    def __init__(self, ability: AbilityScore, weapon: Weapon = Weapon(), attack_mod = None):
        self.ability = ability
        self.weapon = weapon
        self.attack_mod = attack_mod if attack_mod is not None else self.ability.str_mod

    def weapon_damage_roll(self, weapon: Weapon):
        return Dice.roll(weapon.roll)

    def attack_modifier(self, weapon: Weapon):
        return self.ability.prof + self.attack_mod() + weapon.attack

    def attack_damage_modifier(self, weapon: Weapon):
        return self.attack_mod() + weapon.damage

    def attack_roll(self, weapon: Weapon, adv: int):
        if adv > 0:
            roll = Dice.advantage(Dice.d20)
        elif adv < 0:
            roll = Dice.disadvantage(Dice.d20)
        else:
            roll = Dice.d20()
        print("Attack roll", roll, self.attack_modifier(weapon))
        return (roll + self.attack_modifier(weapon), Dice.isCritSuccess(roll))

    def attack_damage_roll(self, weapon: Weapon):
        return self.weapon_damage_roll(weapon)

    def attack(self, weapon: Weapon = None, adv: int = 0) -> Damage:
        if weapon is None:
            weapon = self.weapon
        attack_roll = self.attack_roll(weapon, adv)
        damage_roll = self.attack_damage_roll(weapon)

        #Crit!
        if attack_roll[1]:
            damage_roll = damage_roll * 2

        print("Attack Damage", damage_roll, self.attack_damage_modifier(weapon))

        return Damage(attack_roll[0], damage_roll + self.attack_damage_modifier(weapon))

    def attack_action(self, weapon: Weapon = None, adv: int = 0) -> List:
        return [self.attack(weapon, adv)]
    
    def bonus_attack(self, weapon: Weapon = None, adv: int = 0):
        return self.attack(weapon, adv)
    
    def bonus_attack_action(self, weapon: Weapon = None, adv: int = 0) -> List:
        return [self.bonus_attack(weapon, adv)]
    
    def full_attack_action(self, weapon: Weapon = None, adv: int = 0) -> List:
        return self.attack_action(weapon, adv) + self.bonus_attack_action(weapon, adv)