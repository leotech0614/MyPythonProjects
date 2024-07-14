"""
File: StoneMasonKarel.py
Name: leo HUNG
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at street 1, avenue 1, facing East.
    post-condition: Karel is at street 1, avenue 13, facing East.
    """
    while front_is_clear():
        up_ready_for_sliding_down()
        move_4_steps()
    up_ready_for_sliding_down()


def up_ready_for_sliding_down():
    """
    pre-condition: Karel is at the bottom of pillar(street 1), facing East.
    post-condition: Karel is at the top of pillar, facing South, ready for sliding down.
    """
    turn_left()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        else:
            move()
    if not on_beeper():
        put_beeper()
    for i in range(2):
        turn_left()
    down()


def down():
    """
    pre-condition: Karel is at the top of pillar, facing South, ready for sliding down.
    post-condition: Karel is at the bottom of pillar(street 1), facing East.
    """
    while front_is_clear():
        move()
    turn_left()


def move_4_steps():
    """
    Karel will move to the next pillar, facing East.
    """
    for i in range(4):
        move()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
