"""
File: CollectNewspaperKarel.py
Name: leo HUNG
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at the street 4, Avenue 3, facing East without holding newspaper.
    post-condition: Karel is at the street 4, Avenue 3, facing East without holding newspaper.
    """
    move_to_newspaper()
    bring_it_home_and_read()


def move_to_newspaper():
    """
    pre-condition: Karel is at the street 4, Avenue 3, facing East without holding newspaper.
    post-condition: Karel is at the street 3, Avenue 6, picking up the newspaper.
    """
    turn_right()
    move()
    turn_left()
    move_3_steps()
    pick_beeper()


def turn_right():
    for i in range(3):
        turn_left()


def move_3_steps():
    for i in range(3):
        move()


def bring_it_home_and_read():
    """
    pre-condition: Karel is at the street 3, Avenue 6, picking up the newspaper.
    post-condition: Karel is at the street 4, Avenue 3, facing East without holding newspaper.
    """
    turn_left()
    turn_left()
    move_3_steps()
    turn_right()
    move()
    turn_right()
    put_beeper()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
