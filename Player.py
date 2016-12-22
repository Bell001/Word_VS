import arcade
import arcade.key
from random import randint


class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y
        self.angle = 0

    def hit(self, other, hit_size):
        return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)

class P1(Model):

    DIR_HORIZONTAL = 0
    DIR_VERTICAL = 1

    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
        self.world = world
        self.x = x
        self.y = y
        self.direction = P1.DIR_VERTICAL

    def switch_direction(self):
        if self.direction == P1.DIR_HORIZONTAL:
            self.direction = P1.DIR_VERTICAL
        else:
            self.direction = P1.DIR_HORIZONTAL

    def animate(self, delta):

        if self.direction == P1.DIR_VERTICAL:
            if self.y > self.world.height:
                self.y = 0
            self.y += 5
        else:
            if self.x > self.world.width:
                self.x = 0
            self.x += 5

    def animate_start(self, delta):

            if self.x > self.world.width:
                self.x = 0
            self.x += 3

    def animate_end(self, delta):

        if self.y > self.world.height:
            self.y = 0
        self.y += 2

class P2(Model):
    DIR_HORIZONTAL = 0
    DIR_VERTICAL = 1

    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
        self.world = world
        self.x = x
        self.y = y
        self.direction = P1.DIR_VERTICAL

    def switch_direction(self):
        if self.direction == P1.DIR_HORIZONTAL:
            self.direction = P1.DIR_VERTICAL
        else:
            self.direction = P1.DIR_HORIZONTAL

    def animate(self, delta):
        if self.direction == P1.DIR_VERTICAL:
            if self.y > self.world.height:
                self.y = 0
            self.y += 5
        else:
            if self.x > self.world.width:
                self.x = 0
            self.x += 5


    def animate_start(self, delta):

         if self.y > self.world.height:
                self.y = 0
         self.y += 2

    def animate_end(self, delta):

        if self.x > self.world.width:
            self.x = 0
        self.x += 3

class Box(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
        self.world = world
        self.x = x
        self.y = y

    def random_location(self):
        self.x = randint(0, self.world.width - 1)
        self.y = randint(0, self.world.height - 1)


class World:

    MOVEMENT_SPEED = 2
    START_1 = 1

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.score = 0

        self.play1 = P1(self,100, 100)
        self.play2 = P2(self,100,200)
        self.box =  Box(self, 300 ,300)

    def animate(self, delta):
        self.play1.animate(delta)
        self.play2.animate(delta)

        if self.play1.hit(self.box, 50):
            self.play1.x -= 2

    def animate_start(self, delta):
        self.play1.animate_start(delta)
        self.play2.animate_start(delta)

    def animate_end(self, delta):
        self.play1.animate_end(delta)
        self.play2.animate_end(delta)


    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.play1.switch_direction()
        if key == arcade.key.RIGHT:
            self.play2.switch_direction()
        if key == arcade.key.UP:
            self.play1.y += self.MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.play1.y += -self.MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.play1.x += -self.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.play1.x += self.MOVEMENT_SPEED

    def setdirection(self):
        if self.START_1 == 1:
            self.play1.x = 100
            self.play1.y = 100
            self.play2.x = 100
            self.play2.y = 200
            self.START_1 = 0

