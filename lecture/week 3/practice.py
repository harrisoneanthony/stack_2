import random
import math

class Robot:
    def __init__(self, name, weapon, weapon_damage, shield, speed):
        self.name = name
        self.weapon = weapon
        self.weapon_damage = weapon_damage
        self.speed = speed
        self.shield = shield
        self.health = 100
        if shield:
            self.defense = 100
        else:
            self.defense = 50

    def attack(self, target):
        if math.floor(random.random() * 21) > target.speed:
            if target.defense == 100:
                target.health -= self.weapon_damage / 2
            else:
                target.health -= self.weapon_damage
            print("hit", target.health)
        else:
            print("missed!")

gumby = Robot("Gumby", "katana", 9, False, 17,)
Mr_Roboto = Robot("Mr Roboto", "Hammer", 10, True, 5)

print(gumby.defense)
print(Mr_Roboto.defense)

gumby.attack(Mr_Roboto)
Mr_Roboto.attack(gumby)