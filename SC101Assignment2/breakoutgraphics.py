"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
################
moving = True
################


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.rect = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.rect.filled = True
        self.rect.fill_color = 'black'
        self.rect.color = 'black'
        self.window.add(self.rect)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(window_width-ball_radius)/2, y=(window_height-ball_radius)/2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.ball.color = 'black'
        self.window.add(self.ball)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmouseclicked(self.set_ball_velocity)
        onmousemoved(self.change_x_position)
        # Draw bricks
        self._brick_count = 0
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                self.brick = GRect(brick_width, brick_height, x=(brick_width+brick_spacing)*j, y=brick_offset+(brick_height+brick_spacing)*i)
                self._brick_count += 1
                self.brick.filled = True
                if i <= 1:
                    self.brick.fill_color = 'red'
                if 2 <= i <= 3:
                    self.brick.fill_color = 'orange'
                if 4 <= i <= 5:
                    self.brick.fill_color = 'yellow'
                if 6 <= i <= 7:
                    self.brick.fill_color = 'green'
                if 8 <= i <= 9:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick)

    def get_bricks_count(self):
        return self._brick_count

    def set_bricks_count(self, count):
        self._brick_count = count

    def change_x_position(self, mouse):
        self.rect.x = mouse.x - self.rect.width / 2
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x + self.rect.width > self.window.width:
            self.rect.x = self.window.width - self.rect.width

    def set_ball_velocity(self, event):
        global moving
        if moving:
            moving = False
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx
        # print(moving)  # Debug print

    def reset_ball(self):
        global moving
        moving = True
        self.ball.x = (self.window.width - self.ball.width)/2
        self.ball.y = (self.window.height - self.ball.width)/2
        self.__dx = 0
        self.__dy = 0
        # print(moving)  # Debug print

    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    def set_vx(self, new_vx):
        self.__dx = new_vx

    def set_vy(self, new_vy):
        self.__dy = new_vy



