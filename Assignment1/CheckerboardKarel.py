"""
File: CheckerboardKarel.py
Name: leo HUNG
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at street 1, avenue 1, facing East.
    post-condition: Karel is at avenue 1 with the wall on the right-hand side, facing West.
    """
    fill_the_odd_avenue_in_odd_streets()
    while right_is_clear():
        if on_beeper():
            turn_around()
            fill_the_even_avenue_in_even_streets()
        else:
            turn_around()
            fill_the_odd_avenue_in_odd_streets()


def turn_right():
    """
    Karel will turn left 3 times
    """
    for i in range(3):
        turn_left()


def turn_around():
    """
    Karel will turn to the next starting site.
    """
    turn_right()
    move()
    turn_right()


def fill_the_odd_avenue_in_odd_streets():
    """
    pre-condition: Karel is at odd street, avenue 1, facing East.
    post-condition: Karel is at the origin point before the filling started, facing West.
    """
    put_beeper()
    while front_is_clear():
        if not on_beeper():
            move()
            put_beeper()
        else:
            move()
    back_to_the_origin_point()


def back_to_the_origin_point():
    """
    pre-condition: Karel is facing East and the wall is right ahead.
    post-condition: Karel is at the origin point before the filling started, facing West.
    """
    for i in range(2):
        turn_left()
    while front_is_clear():
        move()


def fill_the_even_avenue_in_even_streets():
    """
    pre-condition: Karel is at even street, avenue 1, facing East.
    post-condition: Karel is at the origin point before the filling started, facing West.
    """
    while front_is_clear():
        if not on_beeper():
            move()
            put_beeper()
        else:
            move()
    back_to_the_origin_point()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
