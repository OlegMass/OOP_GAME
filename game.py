import time
import random


# data = {"level" : 1, 
#         "experiance": 0, 
#         "boss_level": 1,
#         "life": 100,
#         "defence"
#         }

class Creator:
    def __init__(self, life, defense, damage):
        self.level = 1
        self.experience = 0
        self.life = life
        self.defense = defense
        self.damage = damage
        self.critical = 10

    def attack(self, user):
        user.life -= self.damage - user.defense

    def experiance(self):
        pass


hero = Creator(100, 20, 30)

creature = Creator(40, 10, 50)


def attack_creature():
    creature_num = int(input("""
        How many Creatures do you want to attack?
    """))

    while True:
        input("Press enter to punch an enemy")
        time.sleep(1)
        hero.attack(creature)
        if creature.life <= 0 and creature_num == 1:
            print('You win!')
            break
        elif creature.life <= 0 and creature_num > 1:
            creature_num -= 1
            print(f"You kill 1 creature and {creature_num} creatures are left ")
            creature.life = 40

        print(f"Creature has {creature.life} life.")
        time.sleep(1)
        print("Creature attacking you too!!!")
        for i in range(creature_num):
            creature.attack(hero)
            if hero.life <= 0:
                print('You are dead!')
                break
            
            print(f"You have {hero.life} life.")
            
        if hero.life <= 0:
            break
        


def main():

    print(""" 
            1 Attack creatures
            2 Attack Boss
    """)
    choice = int(input("What do you want to do?"))
    if choice == 1:
        attack_creature()

main()




