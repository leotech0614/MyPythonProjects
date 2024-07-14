"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from extension_breakoutgraphics import BreakoutGraphics
from campy.graphics.gimage import GImage
from campy.graphics.gobjects import GOval, GRect, GLabel
import random

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3  		    # Number of attempts
num_wall = 0


def main():
    graphics = BreakoutGraphics()
    # import Lives' picture
    img1 = GImage('123.png')
    img2 = GImage('123.png')
    img3 = GImage('123.png')
    graphics.window.add(img1, x=img1.width * 0, y=graphics.window.height - img1.height)
    graphics.window.add(img2, x=img2.width * 1, y=graphics.window.height - img2.height)
    graphics.window.add(img3, x=img3.width * 2, y=graphics.window.height - img3.height)
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
            if NUM_LIVES == 2:
                graphics.window.remove(img3)
            if NUM_LIVES == 1:
                graphics.window.remove(img2)
            if NUM_LIVES == 0:
                graphics.window.remove(img1)
                score_label = GLabel('Game over')
                score_label.font = '-95'
                score_label.color = 'red'
                graphics.window.add(score_label, x=0, y=graphics.window.height/2+100)
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
            if ball1 == graphics.img_tennis or ball2 == graphics.img_tennis or ball3 == graphics.img_tennis or ball4 == graphics.img_tennis:
                #  only one rect
                if graphics.img_tennis.y < graphics.ball.y + graphics.ball.height:
                    graphics.ball.y = graphics.img_tennis.y - graphics.ball.height
                # Reset ball's location in case of getting stuck in the paddle and oscillates up and down
                vy = -vy
                graphics.set_vy(vy)
            elif ball1 == img1 or ball2 == img1 or ball3 == img1 or ball4 == img1:
                pass
            elif ball1 == img2 or ball2 == img2 or ball3 == img2 or ball4 == img2:
                pass
            elif ball1 == img3 or ball2 == img3 or ball3 == img3 or ball4 == img3:
                pass
            elif ball1 == graphics.tennis_rect1 or ball2 == graphics.tennis_rect1 or ball3 == graphics.tennis_rect1 or ball4 == graphics.tennis_rect1:
                pass
            elif ball1 == graphics.tennis_rect2 or ball2 == graphics.tennis_rect2 or ball3 == graphics.tennis_rect2 or ball4 == graphics.tennis_rect2:
                pass
            elif ball1 == graphics.tennis_rect3 or ball2 == graphics.tennis_rect3 or ball3 == graphics.tennis_rect3 or ball4 == graphics.tennis_rect3:
                pass
            elif ball1 == graphics.tennis_rect4 or ball2 == graphics.tennis_rect4 or ball3 == graphics.tennis_rect4 or ball4 == graphics.tennis_rect4:
                pass
            elif ball1 == graphics.tennis_rect5 or ball2 == graphics.tennis_rect5 or ball3 == graphics.tennis_rect5 or ball4 == graphics.tennis_rect5:
                pass
            elif ball1 == graphics.tennis_rect6 or ball2 == graphics.tennis_rect6 or ball3 == graphics.tennis_rect6 or ball4 == graphics.tennis_rect6:
                pass
            elif ball1 == graphics.score_label or ball2 == graphics.score_label or ball3 == graphics.score_label or ball4 == graphics.score_label:
                pass
            else:
                count = graphics.get_bricks_count()
                count -= 1
                global num_wall
                if ball1:
                    brick1 = ball1
                    graphics.window.remove(brick1)
                    # print(brick1.fill_color.b)
                    # print(brick1.fill_color.g)
                    # print(brick1.fill_color.r)  # Debug print
                    if brick1.fill_color.r == 0 and brick1.fill_color.g == 0 and brick1.fill_color.b == 255:
                        graphics.score += 2
                    if brick1.fill_color.r == 0 and brick1.fill_color.g == 128 and brick1.fill_color.b == 0:
                        graphics.score += 4
                    if brick1.fill_color.r == 255 and brick1.fill_color.g == 255 and brick1.fill_color.b == 0:
                        graphics.score += 6
                    if brick1.fill_color.r == 255 and brick1.fill_color.g == 200 and brick1.fill_color.b == 0:
                        graphics.score += 8
                    if brick1.fill_color.r == 255 and brick1.fill_color.g == 0 and brick1.fill_color.b == 0:
                        graphics.score += 10
                    if brick1.fill_color.r == 0 and brick1.fill_color.g == 0 and brick1.fill_color.b == 0:
                        graphics.reset_ball2()
                        count += 1
                        num_wall -= 1

                elif ball2:
                    brick2 = ball2
                    graphics.window.remove(brick2)
                    if brick2.fill_color.r == 0 and brick2.fill_color.g == 0 and brick2.fill_color.b == 255:
                        graphics.score += 2
                    if brick2.fill_color.r == 0 and brick2.fill_color.g == 128 and brick2.fill_color.b == 0:
                        graphics.score += 4
                    if brick2.fill_color.r == 255 and brick2.fill_color.g == 255 and brick2.fill_color.b == 0:
                        graphics.score += 6
                    if brick2.fill_color.r == 255 and brick2.fill_color.g == 200 and brick2.fill_color.b == 0:
                        graphics.score += 8
                    if brick2.fill_color.r == 255 and brick2.fill_color.g == 0 and brick2.fill_color.b == 0:
                        graphics.score += 10
                    if brick2.fill_color.r == 0 and brick2.fill_color.g == 0 and brick2.fill_color.b == 0:
                        graphics.reset_ball2()
                        count += 1
                        num_wall -= 1

                elif ball3:
                    brick3 = ball3
                    graphics.window.remove(brick3)
                    if brick3.fill_color.r == 0 and brick3.fill_color.g == 0 and brick3.fill_color.b == 255:
                        graphics.score += 2
                    if brick3.fill_color.r == 0 and brick3.fill_color.g == 128 and brick3.fill_color.b == 0:
                        graphics.score += 4
                    if brick3.fill_color.r == 255 and brick3.fill_color.g == 255 and brick3.fill_color.b == 0:
                        graphics.score += 6
                    if brick3.fill_color.r == 255 and brick3.fill_color.g == 200 and brick3.fill_color.b == 0:
                        graphics.score += 8
                    if brick3.fill_color.r == 255 and brick3.fill_color.g == 0 and brick3.fill_color.b == 0:
                        graphics.score += 10
                    if brick3.fill_color.r == 0 and brick3.fill_color.g == 0 and brick3.fill_color.b == 0:
                        graphics.reset_ball2()
                        count += 1
                        num_wall -= 1

                elif ball4:
                    brick4 = ball4
                    graphics.window.remove(brick4)
                    if brick4.fill_color.r == 0 and brick4.fill_color.g == 0 and brick4.fill_color.b == 255:
                        graphics.score += 2
                    if brick4.fill_color.r == 0 and brick4.fill_color.g == 128 and brick4.fill_color.b == 0:
                        graphics.score += 4
                    if brick4.fill_color.r == 255 and brick4.fill_color.g == 255 and brick4.fill_color.b == 0:
                        graphics.score += 6
                    if brick4.fill_color.r == 255 and brick4.fill_color.g == 200 and brick4.fill_color.b == 0:
                        graphics.score += 8
                    if brick4.fill_color.r == 255 and brick4.fill_color.g == 0 and brick4.fill_color.b == 0:
                        graphics.score += 10
                    if brick4.fill_color.r == 0 and brick4.fill_color.g == 0 and brick4.fill_color.b == 0:
                        graphics.reset_ball2()
                        count += 1
                        num_wall -= 1
                # count
                graphics.set_bricks_count(count)
                # score
                graphics.score_label.text = 'Score: ' + str(graphics.score)
                if graphics.score > 0:
                    if vx >= 0:
                        vx += 0.01 * graphics.score
                    else:
                        vx -= 0.01 * graphics.score
                    if vx >= 9:
                        vx = 9
                    if vx <= -9:
                        vx = -9
                    graphics.set_vx(vx)  # Update the velocity in the graphics object
                # velocity
                vy = -vy
                graphics.set_vy(vy)
                # print(count)  # Debug print
                if count <= 50:
                    if num_wall == 0:
                        graphics.appear_wall()
                        num_wall += 1
                if count == 0:
                    graphics.reset_ball()
                    score_label = GLabel(' '*7+'Congrats!!\n All bricks cleared')
                    score_label.font = '-60'
                    score_label.color = 'red'
                    graphics.window.add(score_label, x=0, y=graphics.window.height / 2 + 57)
                    break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
