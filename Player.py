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
    MOVE_SPEED = 5

    MOVE = 0

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

        if self.y > self.world.height:
            self.y = 1
            self.y  += self.MOVE_SPEED
        if self.x > self.world.width:
            self.x = 1
            self.x += self.MOVE_SPEED
        if self.y < 0:
            self.y = self.world.height-1
            self.y -= self.MOVE_SPEED
        if self.x < 0:
            self.x = self.world.width-1
            self.x -= self.MOVE_SPEED


        if self.MOVE == 1:
            self.y += self.MOVE_SPEED
        elif self.MOVE == 2:
            self.y -= self.MOVE_SPEED
        elif self.MOVE == 3:
            self.x -= self.MOVE_SPEED
        elif self.MOVE == 4:
            self.x += self.MOVE_SPEED
        elif self.MOVE == 0:
            self.x += 0
            self.y += 0

    def animate_start(self, delta):

            if self.x > self.world.width:
                self.x = 0
            self.x += 3

    def animate_end(self, delta):

        if self.y > self.world.height:
            self.y = 0
        self.y += 2

class P2(Model):

    MOVE_SPEED = 5

    MOVE = 0

    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
        self.world = world
        self.x = x
        self.y = y

    def animate(self, delta):

        if self.y > self.world.height:
            self.y = 1
            self.y  += self.MOVE_SPEED
        if self.x > self.world.width:
            self.x = 1
            self.x += self.MOVE_SPEED
        if self.y < 0:
            self.y = self.world.height-1
            self.y -= self.MOVE_SPEED
        if self.x < 0:
            self.x = self.world.width-1
            self.x -= self.MOVE_SPEED

        if self.MOVE == 1:
            self.y += self.MOVE_SPEED
        elif self.MOVE == 2:
            self.y -= self.MOVE_SPEED
        elif self.MOVE == 3:
            self.x -= self.MOVE_SPEED
        elif self.MOVE == 4:
            self.x += self.MOVE_SPEED
        elif self.MOVE == 0:
            self.x += 0
            self.y += 0


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

    def animate(self, delta):
        self.x += 0

    def random_location(self):
        self.x = randint(0, self.world.width - 1)
        self.y = randint(0, self.world.height - 1)

class Ice(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
        self.world = world
        self.x = x
        self.y = y

    def animate(self, delta):
        self.x += 0

    def random_location(self):
        self.x = randint(0, self.world.width - 1)
        self.y = randint(0, self.world.height - 1)


class Star(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
        self.world = world
        self.x = x
        self.y = y

    def animate(self, delta):
        self.x += 0

    def random_location(self):
        self.x = randint(0, self.world.width - 1)
        self.y = randint(0, self.world.height - 1)


class Time(Model):
    def __init__(self, world, x, y):
        super().__init__(world, x, y, 0)
        self.world = world
        self.x = x
        self.y = y

    def animate(self, delta):
        self.x += 0

    def random_location(self):
        self.x = randint(0, self.world.width - 1)
        self.y = randint(0, self.world.height - 1)



class World:

    MOVEMENT_SPEED = 10
    START_1 = 1
    P1_CANMOVE = True
    P2_CANMOVE = True
    SCORE_SOM =0
    SCORE_UFO =0
    SCORE_TURN = [SCORE_SOM,SCORE_UFO]
    POINT_SOM = 0
    POINT_UFO = 0

    POINT_TURN = [POINT_SOM,POINT_UFO]
    TURN = 0

    TIMER = 0
    CANMOVE_TIME = 5
    COUNT_TIME = False
    TIMELIMIT = 60

    OUTPUT = ' '
    TIMEOUT =0

    def __init__(self, width, height):

        self.width = width
        self.height = height
        self.score = 0
        self.total_time = 0.0
        self.TURN = randint(0,1)

        self.som = P1(self,400, 400)
        self.ufo = P2(self,100,200)
        self.player_turn = [self.som,self.ufo]
        self.point_turn = [self.POINT_SOM,self.POINT_UFO]

        self.box1 =  Box(self, randint(0, self.width - 1), randint(0, self.height - 1))
        self.box2 = Box(self, randint(0, self.width - 1), randint(0, self.height - 1))
        self.box3 = Box(self, randint(0, self.width - 1), randint(0, self.height - 1))
        self.box4 = Box(self, randint(0, self.width - 1), randint(0, self.height - 1))
        self.box5 = Box(self, randint(0, self.width - 1), randint(0, self.height - 1))
        self.box6 = Box(self, randint(0, self.width - 1), randint(0, self.height - 1))

        self.list_box = [self.box1,self.box2,self.box3,self.box4,self.box5,self.box6]

        self.star = Star(self, randint(0, self.width - 1), randint(0, self.height - 1))
        self.ice1 = Ice(self, randint(0, self.width - 1), randint(0, self.height - 1))
        self.time = Time(self, randint(0, self.width - 1), randint(0, self.height - 1))

    def animate(self, delta):

        seconds = int(self.total_time)
        self.OUTPUT = "Time: {:02d}".format(self.TIMELIMIT - seconds)
        self.TIMEOUT = int(self.TIMELIMIT-seconds)

        self.som.animate(delta)
        self.ufo.animate(delta)

        for a in self.list_box:
            a.animate(delta)

            if self.player_turn[self.TURN].hit(a, 50):
                a.random_location()
                self.SCORE_TURN[self.TURN] += 5
            if self.TURN == 0:
                if self.player_turn[self.TURN+1].hit(a, 50):
                    a.random_location()
                    self.SCORE_TURN[self.TURN] -= 5
            if self.TURN == 1:
                if self.player_turn[self.TURN-1].hit(a, 50):
                    a.random_location()
                    self.SCORE_TURN[self.TURN] -= 5


        self.can_not_move()

        if self.som.hit(self.star , 50):
            self.star.random_location()
            self.score += 10
        if self.ufo.hit(self.star, 50):
            self.star.random_location()
            self.score -= 10

        if self.som.hit(self.time, 50):
            self.time.random_location()
            self.TIMELIMIT += 5
        if self.ufo.hit(self.time, 50):
            self.time.random_location()
            self.TIMELIMIT += 5


        if self.COUNT_TIME == True:
            self.CANMOVE_TIME -= delta

        if self.CANMOVE_TIME <= 0:
            self.P1_CANMOVE = True
            self.P2_CANMOVE = True
            self.COUNTTIME = False
            self.CANMOVE_TIME = 5

        self.total_time += delta




    def animate_start(self, delta):
        self.som.animate_start(delta)
        self.ufo.animate_start(delta)

    def animate_end(self, delta):
        self.som.animate_end(delta)
        self.ufo.animate_end(delta)


    def on_key_press(self, key, key_modifiers):

      if self.P1_CANMOVE:
        if key == arcade.key.UP:
            self.som.MOVE  = 1
        elif key == arcade.key.DOWN:
            self.som.MOVE  = 2
        elif key == arcade.key.LEFT:
            self.som.MOVE = 3
        elif key == arcade.key.RIGHT:
            self.som.MOVE = 4
      else:
          self.som.MOVE = 0

      if self.P2_CANMOVE:
        if key == arcade.key.W:
            self.ufo.MOVE = 1
        elif key == arcade.key.S:
            self.ufo.MOVE = 2
        elif key == arcade.key.A:
            self.ufo.MOVE = 3
        elif key == arcade.key.D:
            self.ufo.MOVE = 4
      else:
          self.ufo.MOVE = 0


    def setdirection(self):
        if self.START_1 == 1:
            self.som.x = 400
            self.som.y = 400
            self.ufo.x = 100
            self.ufo.y = 200
            self.START_1 = 0

    def can_not_move(self):

        if self.som.hit(self.ice1, 50):
            self.ice1.random_location()
            self.P2_CANMOVE = False
            self.COUNT_TIME = True

        if self.ufo.hit(self.ice1, 50):
            self.ice1.random_location()
            self.P1_CANMOVE = False
            self.COUNT_TIME = True



