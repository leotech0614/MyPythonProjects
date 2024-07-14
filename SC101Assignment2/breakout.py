"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gimage import GImage
from campy.graphics.gobjects import GOval, GRect, GLabel
import random

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add the animation loop here!
    global NUM_LIVES
    while True:
        vx = graphics.get_vx()
        vy = graphics.get_vy()
        # print("Velocity set to: vx =", vx, ", vy =", vy)  # Debug print
        graphics.ball.move(vx, vy)
        if graphics.ball.y > graphics.window.height:
            graphics.reset_ball()
            NUM_LIVES -= 1
            if NUM_LIVES == 0:
                print('Game over')
                break
        if graphics.ball.x + graphics.ball.width >= graphics.window.width or graphics.ball.x < 0:
            vx = -vx
            graphics.set_vx(vx)  # Update the velocity in the graphics object
        if graphics.ball.y <= 0:
            vy = -vy
            graphics.set_vy(vy)  # Update the velocity in the graphics object

        ball1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        ball2 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height)
        ball3 = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y)
        ball4 = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y+graphics.ball.height)

        if ball1 is not None or ball2 is not None or ball3 is not None or ball4 is not None:
            if ball1 == graphics.rect or ball2 == graphics.rect or ball3 == graphics.rect or ball4 == graphics.rect:
                #  only one rect
                if graphics.rect.y < graphics.ball.y + graphics.ball.height:
                    graphics.ball.y = graphics.rect.y - graphics.ball.height
                # Reset ball's location in case of getting stuck in the paddle and oscillates up and down
                vy = -vy
                graphics.set_vy(vy)
            else:
                count = graphics.get_bricks_count()
                count -= 1
                if ball1:
                    brick1 = ball1
                    graphics.window.remove(brick1)

                elif ball2:
                    brick2 = ball2
                    graphics.window.remove(brick2)

                elif ball3:
                    brick3 = ball3
                    graphics.window.remove(brick3)

                elif ball4:
                    brick4 = ball4
                    graphics.window.remove(brick4)

                graphics.set_bricks_count(count)

                vy = -vy
                graphics.set_vy(vy)
                # print(count)  # Debug print
                if count == 0:
                    print('Congrats!!\n All bricks cleared')
                    break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
