"""
File: draw line
Name: leo HUNG
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the hole
SIZE = 10
# Global Variable
window = GWindow()

click = 1
a = 0
b = 0

hole1 = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(create_line)


def create_line(mouse):
    global click
    global a
    global b

    if click % 2 == 1:
        hole1.filled = False
        hole1.color = 'black'
        window.add(hole1, x=mouse.x-SIZE//2, y=mouse.y-SIZE//2)
        click += 1
        a = hole1.x + SIZE//2
        b = hole1.y + SIZE//2
    else:
        old_hole = window.get_object_at(a, b)
        window.remove(old_hole)
        line = GLine(a, b, mouse.x, mouse.y)
        window.add(line)
        click -= 1
        a = 0
        b = 0


if __name__ == "__main__":
    main()