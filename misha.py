
import copy
from ast import List
from dice import Dice
from character import AbilityScore, Weapon, Damage, Character

class Misha(Character):
    def __init__(self):
        ability = AbilityScore(3, 20, 12, 15, 9, 13, 10)
        weapon = Weapon(1, 1, [Dice.d10])
        super().__init__(ability, weapon)
    
    def rage(self):
        self.weapon.damage = self.weapon.damage + 2
    
    def great_weapon_attack(self, weapon: Weapon = None, adv: int = 0) -> List:
        mod_weap = copy.deepcopy(weapon if weapon is not None else self.weapon)
        mod_weap.damage = mod_weap.damage + 10
        mod_weap.attack = mod_weap.attack - 5
        return [self.attack(mod_weap, adv)]

    def attack_action(self, weapon: Weapon = None, adv: int = 0) -> List:
        return [self.attack(weapon, adv), self.attack(weapon, adv)]
    
    def great_weapon_attack_action(self, weapon: Weapon = None, adv: int = 0) -> List:
        mod_weap = copy.deepcopy(weapon if weapon is not None else self.weapon)
        mod_weap.damage = mod_weap.damage + 10
        mod_weap.attack = mod_weap.attack - 5
        return self.attack_action(mod_weap, adv)

    def full_attack_action(self, weapon: Weapon = None, adv: int = 0) -> List:
        return self.attack_action(weapon, adv)
    
    def frenzy_full_attack_action(self, weapon: Weapon = None, adv: int = 0) -> List:
        return self.attack_action(weapon, adv) + self.bonus_attack_action(weapon, adv)
    
    def frenzy_gw_full_attack_action(self, weapon: Weapon = None, adv: int = 0) -> List:
        return self.great_weapon_attack_action(weapon, adv) + self.great_weapon_attack(weapon, adv)