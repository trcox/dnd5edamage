import copy
from ast import List
from dice import Dice
from character import AbilityScore, Weapon, Damage, Character

class Sheraz(Character):
    def __init__(self):
        ability = AbilityScore(3, 8, 19, 14, 18, 15, 16)
        self.crossbow = Weapon(1, 1, [Dice.d6])
        self.rapier = Weapon(0, 0, [Dice.d8])
        super().__init__(ability, self.rapier, attack_mod=ability.dex_mod)
    
    def sneak_attack(self, weapon: Weapon = None, adv: int = 0) -> List:
        mod_weap = copy.deepcopy(weapon if weapon is not None else self.weapon)
        mod_weap.roll = mod_weap.roll + [Dice.d6, Dice.d6, Dice.d6]
        return [self.attack(mod_weap, adv)]

    def attack_action(self, weapon: Weapon = None, adv: int = 0) -> List:
        return [self.attack(weapon if weapon is not None else self.rapier, adv)]
    
    def bonus_attack_action(self, weapon: Weapon = None, adv: int = 0) -> List:
        return [self.bonus_attack(weapon if weapon is not None else self.crossbow, adv)]
    
    def full_attack_action(self, adv: int = 0) -> List:
        return self.attack_action(self.rapier, adv) + self.sneak_attack(self.crossbow, adv)