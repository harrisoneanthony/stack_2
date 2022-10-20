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
                print(f'{self.name} hit {target.name} for {self.weapon_damage/2} now {target.name} health is {target.health}')
            else:
                target.health -= self.weapon_damage
                print(f'{self.name} hit {target.name} for {self.weapon_damage} now {target.name} health is {target.health}')
        else:
            print(f'{target.name} dodged {self.name}s attack')

    @classmethod
    def battle(cls, robot_1, robot_2):
        print(("Let's get ready to rumbllllllle!!!"))
        while robot_1.health > 0 and robot_2.health > 0:
            robot_1.attack(robot_2)
            robot_2.attack(robot_1)
        if robot_1.health == 0:
            print(robot_1.name)
        else: 
            print(robot_2.name)



gumby = Robot("Gumby", "katana", 9, False, 17,)
Mr_Roboto = Robot("Mr Roboto", "Hammer", 10, True, 5)

print(gumby.defense)
print(Mr_Roboto.defense)

gumby.attack(Mr_Roboto)
Mr_Roboto.attack(gumby)

Robot.battle(gumby, Mr_Roboto)