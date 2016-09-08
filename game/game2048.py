import curses
from random import randrange, choice
from collections import defaultdict

# actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']

# letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']

# actions_dict = dict(zip(letter_codes, actions * 2))
actions_dict = {65: 'Left', 115: 'Down', 68: 'Right', 97: 'Left', 119: 'Up', 114: 'Restart', 81: 'Exit', 82: 'Restart', 83: 'Down', 113: 'Exit', 87: 'Up', 100: 'Right'}

def curses_main(args):
    keyboard = curses.initscr()
    char = "N"
    while char not in actions_dict:
        char = keyboard.getch()
        keyboard.insertln()
        keyboard.addstr(1, 0, "[" +"]")
        if(char=='q'): break

curses.wrapper(curses_main)
