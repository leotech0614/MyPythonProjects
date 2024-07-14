"""
File: extension1_MidpointKarel.py
Name: leo HUNG
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at (1,1), facing East. #(1,1) mean street 1, avenue 1
    post-condition: Karel is at the middle avenue of the street 1.
    """
    going_diagonally_up_to_the_right()
    sliding_to_avenue1()
    going_diagonally_down_to_the_left_until_on_beeper()
    sliding_to_street1()
    put_beeper()
    back_to_1_1()
    pick_all_beepers()
    go_to_the_middle_beeper()
    put_beeper()
    pick_beeper()


def going_diagonally_up_to_the_right():
    """
    Karel will go diagonally up to the right by using the stairs.
    """
    put_beeper()
    while front_is_clear():
        move()
        turn_left()
        move()
        put_beeper()
        turn_right()
    sliding_to_avenue1()


def turn_right():
    """
    Karel will turn left 3 times.
    """
    for i in range(3):
        turn_left()


def sliding_to_avenue1():
    """
    Karel will sliding to avenue1.
    """
    while not facing_west():
        turn_left()
    while front_is_clear():
        move()
    turn_around()


def turn_around():
    """
    Karel will turn left 2 times.
    """
    for i in range(2):
        turn_left()


def going_diagonally_down_to_the_left_until_on_beeper():
    """
    Karel will go diagonally down to the left by using the stairs until on beeper.
    """
    while not on_beeper():
        move()
        turn_right()
        if not on_beeper():
            move()
            turn_left()
    while not facing_south():
        turn_left()


def sliding_to_street1():
    """
    Karel will sliding to street1.
    """
    while front_is_clear():
        move()


def back_to_1_1():
    """
    Karel will back to (1,1).
    """
    turn_right()
    while front_is_clear():
        move()
    turn_around()


def pick_all_beepers():
    """
    Karel will pick all beepers.
    """
    pick_beeper()
    while front_is_clear():
        move()
        turn_left()
        move()
        pick_beeper()
        turn_right()


def go_to_the_middle_beeper():
    """
    Karel will go to the middle beeper.
    """
    turn_right()
    while front_is_clear():
        move()
    turn_right()
    while not on_beeper():
        move()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
