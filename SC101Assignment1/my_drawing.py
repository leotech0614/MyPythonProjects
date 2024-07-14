"""
File: My cherish doll
Name: leo HUNG
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GArc, GPolygon
from campy.graphics.gwindow import GWindow


SIZE = 300


def main():
    """
    Title: My cherish doll
    This is the teddy bear my girlfriend and I made together to commemorate our anniversary.
    Today, we used the fun programming of SC101 to showcase it on the computer!
    """
    window = GWindow(width=800, height=600, title='My drawing')

    carpet = GOval(550, 150)
    carpet.filled = True
    carpet.fill_color = 'bisque'
    carpet.color = 'bisque'

    face1 = GOval(180, 150)
    face1.filled = True
    face1.fill_color = 'steelblue'
    face1.color = 'steelblue'

    face2 = GOval(150, 170)
    face2.filled = True
    face2.fill_color = 'steelblue'
    face2.color = 'steelblue'

    eye1 = GOval(20, 25)
    eye1.filled = True
    eye1.fill_color = 'black'

    eye2 = GOval(20, 25)
    eye2.filled = True
    eye2.fill_color = 'black'

    ear1 = GOval(85, 85)
    ear1.filled = True
    ear1.fill_color = 'steelblue'
    ear1.color = 'steelblue'

    ear2 = GOval(85, 85)
    ear2.filled = True
    ear2.fill_color = 'steelblue'
    ear2.color = 'steelblue'

    nose = GOval(50, 30)
    nose.filled = True
    nose.fill_color = 'powderblue'
    nose.color = 'powderblue'

    bow_tie = GOval(20, 20)
    bow_tie.filled = True
    bow_tie.fill_color = 'powderblue'
    bow_tie.color = 'powderblue'

    triangle_left = GPolygon()
    triangle_left.add_vertex((10, 30))
    triangle_left.add_vertex((30, 45))
    triangle_left.add_vertex((10, 60))
    triangle_left.filled = True
    triangle_left.fill_color = 'powderblue'
    triangle_left.color = 'powderblue'

    triangle_right = GPolygon()
    triangle_right.add_vertex((10, 30))
    triangle_right.add_vertex((-10, 45))
    triangle_right.add_vertex((10, 60))
    triangle_right.filled = True
    triangle_right.fill_color = 'powderblue'
    triangle_right.color = 'powderblue'

    body = GOval(110, 150)
    body.filled = True
    body.fill_color = 'steelblue'
    body.color = 'steelblue'

    feet1 = GOval(90, 120)
    feet1.filled = True
    feet1.fill_color = 'steelblue'

    feet2 = GOval(90, 120)
    feet2.filled = True
    feet2.fill_color = 'steelblue'

    hand1 = GOval(40, 55)
    hand1.filled = True
    hand1.fill_color = 'steelblue'

    hand2 = GOval(40, 55)
    hand2.filled = True
    hand2.fill_color = 'steelblue'

    arc = GArc(450, 350, 160, 100)

    ballon = GOval(120, 140)
    ballon.filled = True
    ballon.fill_color = 'pink'
    ballon.color = 'pink'

    triangle = GPolygon()
    triangle.add_vertex((10, 30))
    triangle.add_vertex((30, 27))
    triangle.add_vertex((17, 15))
    triangle.filled = True
    triangle.fill_color = 'pink'
    triangle.color = 'pink'

    label = GLabel('SC101')
    label.font = '-38'
    label.color = 'floralwhite'

    window.add(carpet, x=125, y=400)
    window.add(face1, x=310, y=210)
    window.add(face2, x=324, y=150)
    window.add(ear1, x=280, y=130)
    window.add(ear2, x=430, y=130)
    window.add(eye1, x=360, y=228)
    window.add(eye2, x=415, y=228)
    window.add(nose, x=373, y=240)
    window.add(body, x=345, y=330)
    window.add(bow_tie, x=389, y=343)
    window.add(triangle_left, x=365, y=308)
    window.add(triangle_right, x=414, y=308)
    window.add(hand1, x=440, y=340)
    window.add(hand2, x=320, y=340)
    window.add(feet1, x=295, y=380)
    window.add(feet2, x=425, y=380)
    window.add(arc, x=245, y=130)
    window.add(ballon, x=170, y=140)
    window.add(triangle, x=230, y=260)
    window.add(label, x=175, y=233)


if __name__ == '__main__':
    main()
