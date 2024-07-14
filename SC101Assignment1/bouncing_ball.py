"""
File: bouncing ball
Name: leo HUNG
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
window = GWindow(800, 500, title='bouncing_ball.py')
#############
ball = GOval(SIZE, SIZE)
N = 0
VY = 0
bouncing = True  # Use this as a switch.
number = 0  # the number that ball out of range
#############


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(bouncing_ball)


def bouncing_ball(mouse):
    global VY
    global N
    global GRAVITY
    global bouncing
    global number
    if bouncing:
        while True:
            bouncing = False  # Turn off
            ball.move(VX, VY + N * GRAVITY)
            if ball.y + SIZE >= window.height:
                VY = -(VY + N * GRAVITY)
                N = 0
                GRAVITY = GRAVITY / REDUCE
            N += 1
            if ball.x >= window.width:
                ball.x = START_X
                ball.y = START_Y
                number += 1
                if number == 3:
                    bouncing = False  # Turn off
                    break
                else:  # return to starting status
                    VY = 0
                    N = 0
                    GRAVITY = 1
                    bouncing = True  # Turn on
                    break
            pause(10)


if __name__ == "__main__":
    main()
