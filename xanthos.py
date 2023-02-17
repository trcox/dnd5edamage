from ast import List
from dice import Dice
from character import AbilityScore, Weapon, Damage, Character

class Xanthos(Character):
    def __init__(self):
        ability = AbilityScore(3, 16, 18, 14, 12, 15, 10)
        weapon = Weapon(1, 1, [Dice.d6])
        super().__init__(ability, weapon, attack_mod=ability.dex_mod)
    
    def eldritch(self):
        self.weapon.roll.append(Dice.d6)

    def attack_action(self, weapon: Weapon = None, adv: int = 0) -> List:
        return [self.attack(weapon, adv), self.attack(weapon, adv)]
    
    def bonus_attack_action(self, weapon: Weapon = None, adv: int = 0) -> List:
        return [self.bonus_attack(weapon, adv), self.bonus_attack(weapon, adv)]