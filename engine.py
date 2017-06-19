import os
import random

from pyfiglet import Figlet

f = Figlet(font='bigfig')
coliseumArt="""    ________                 
    |-|-|-|.\____________    
    |n|n|n|n|n|n|n|n|n|n|    
    |n|n|n|n|n|n|n|n|n|n|    
    |n|n|n|n|n|n|n|n|n|n|   o
    ~~~~~~~~~~~~~~~~~~~~~   ^
"""


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def press_enter():
    input("\nPress RETURN to return to the Main Menu.")


def logo():
    '''Show the Game Logo'''
    clear_screen()
    print(f.renderText(' Gladiator'))


def about_game():
    logo()
    press_enter()
    pass


def random_name():
    filename=open("resources/names",'r')
    name = random.choice(list(filename)).strip()
    filename.close()
    return name
