'''
Enter a world of glory as a Gladiator. How long can you survive? Can you earn 
enough to buy your freedom?
'''
import random

from engine import *
from characters import *
from art import *

player = False
opponent = False

def menu_loop():
    while True:
        logo()
        art = ["coliseum","mace","sword","axe","flail","staff"]
        #ascii_art(random.choice(art))
        ascii_art("coliseum")
        print("    -MENU"+20*"-")
        print("     Play\n     Scores\n     About\n     Quit")
        action = input("\nAction: ").lower()
        if action == "q" or action == "quit":
            break
        elif action == "p" or action == "play":
            game_loop()
        elif action == "a" or action == "about":
            about_game()
        elif action == "s" or action == "scores":
            show_scores()
    return True


def game_loop():
    new_game()
    #while health > 0 and not free:
    #   training()
    #   shop()
    #   for _ in 5:
    #       battle()
    pass


def new_game():
    clear_screen()
    name = ""
    while name == "":
        name = input("What is your name, fighter? ").strip()
        if name == "":
            print("\nOh the silent type? Don't want to tell me your name?")
            name = input("I can come up with something to call you... [Y/n] ").lower()
            print("")
            if name != "n":
                name = random_name()
                print("Very well. You will be known as {}.".format(name))
            else:
                name = ""
        else:
            print("\n{}... That name has promise. Let's see if you can live up to it.".format(name))
    player = Player(name)
    press_enter()
    pass


def show_scores():
    logo()
    print("There are no scores yet.")
    press_enter()
    pass


if __name__ == '__main__':
    menu_loop()
    clear_screen()
