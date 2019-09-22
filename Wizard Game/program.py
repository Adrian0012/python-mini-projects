# import actors
from datetime import time

from actors import Wizard, Creature, SmallAnimals, Dragon
import random


def main():
    print_header()
    game_loop()


def print_header():
    print('----------------------')
    print('------Wizard Game')
    print('----------------------')


def game_loop():
    creatures = [
        SmallAnimals('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimals('Bat', 3),
        Dragon('Dragon', 50, 75, True),
        Wizard('Evil Wizard', 1000),
    ]

    hero = Wizard('Gandalf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from the dark forrest...'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you want to [a]ttack, [r]unaway or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("Game Over")
                break
            # print("The Wizard runs and hides taking time to recover...")
            # time.sleep(5)
            # print("The Wizard returns revitalized!!")
        elif cmd == 'r':
            print("The Wizard flees!!")
        elif cmd == 'l':
            print("The Wizard {} takes in the surroundings and sees: "
                  .format(hero.name))
            for c in creatures:
                print(" * A {} of level {}".format(c.name, c.level))
        else:
            print('OK, exiting game')
            break

        if not creatures:
            print("You defeated all the monsters!! Well Done!!")


if __name__ == '__main__':
    main()
