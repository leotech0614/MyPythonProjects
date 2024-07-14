"""
File: extension2_MidpointKarel.py
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
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()
    while front_is_clear():
        if on_beeper():
            move()

    # move()
    # while not on_beeper():
    #     move()
    # turn_around()
    # move()
    # put_beeper()
    # move()
    # while not on_beeper():
    #     move()


def turn_around():
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
