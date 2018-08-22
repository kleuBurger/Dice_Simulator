# Dice simulator test

import random
# Importing random

def selection():
# Options for user to choose from
     print("1. Roll dice")
     inp = input("Select an option: ")
     print("")

     while inp == "1":
             return Game()


class Game(object):
# Random number generator for dice throw
        def __init__(self):

            d1 = random.randint(1,12)
            d2 = random.randint(1,12)
            both = (d1 + d2)
            dice = "Dice: %d" % both
            print(dice)


def main():
# Run main program
    return selection()


if __name__ == '__main__':
    main()
