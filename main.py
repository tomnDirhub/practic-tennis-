import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Pong Game"

class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 0.05)
        self.change_x = 3.5
        self.change_y = 3.5

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH:
            self.change_x *= -1
        if self.left <= 0:
            self.change_x *= -1
        if self.top >= SCREEN_HEIGHT:
            self.change_y *= -1
        if self.bottom <= 0:
            self.change_y *= -1

class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 0.13)

    def update(self):
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0

class game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball()
        self.bar = Bar()
        self.setup()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH/2
        self.bar.center_y = SCREEN_HEIGHT/5

        self.ball.center_x = SCREEN_WIDTH/2
        self.ball.center_y = SCREEN_HEIGHT/2

    def on_draw(self):
        self.clear((255, 255, 255))
        self.ball.draw()
        self.bar.draw()

    def update(self, delta):
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y *= -1
        self.ball.update()
        self.bar.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.bar.change_x = 5
        if key == arcade.key.LEFT:
            self.bar.change_x = -5

    def on_key_release(self, key, modifiers):
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0


if __name__ == "__main__":
    window = game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()