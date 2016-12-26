import arcade
import random
import math

from Player import World

SPRITE_SCALING = 1

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

INSTRUCTIONS_PAGE_0 = 0
INSTRUCTIONS_PAGE_1 = 1
GAME_RUNNING = 2
GAME_OVER = 3

SHOOT_SPEED = 5
WORD = [["CAT","HAT","NUT"],["SNOOKER","ICEBEAR","WHITE"],["PENGUIN","PEINNY","SNOWMAN"],["DRAGON","CAT","LION"]]

LOCATION=[[310,600],[410,600],[510,600],[610,600],[710,600]]
NUMSTATUS = [2,1,0,1]
OPC = ' ' #answord from user
NUMC = 0 #number of choice


class ModelSprite(arcade.Sprite):

    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)


    def draw(self):
        self.sync_with_model()
        super().draw()

class SpaceGameWindow(arcade.Window):

    COUNT =0
    NUMB =0
    NumImage = 0
    TIMESET =0
    moveword = 1
    CASE = True
    list =0
    Choice_som = -1
    Choice_ufo = -1
    ChoiceTRUN = [Choice_som,Choice_ufo]
    ORDER =0
    checkans =0
    STOP =0
    Round = ["SOM","UFO"]
    min = 60
    count = True
    a =0

    def __init__(self, width, height):
        super().__init__(width, height)


        arcade.set_background_color(arcade.color.AMAZON)

        self.current_state = INSTRUCTIONS_PAGE_0

        self.instructions = []
        texture = arcade.load_texture("images/start-bg.png")
        self.instructions.append(texture)

        texture = arcade.load_texture("images/running_bg.png")
        self.instructions.append(texture)

        texture = arcade.load_texture("images/end-bg.png")
        self.instructions.append(texture)

        texture = arcade.load_texture("images/START_BG.png")
        self.instructions.append(texture)

        self.world = World(width, height)

        self.play1_sprite = ModelSprite('images/SOM.png',SPRITE_SCALING, model=self.world.som)
        self.play1lose_sprite = ModelSprite('images/SOMSAD.png',SPRITE_SCALING)
        self.play2_sprite = ModelSprite('images/UFO.png',SPRITE_SCALING,model=self.world.ufo)
        self.play2lose_sprite = ModelSprite('images/UFOSAD.png', SPRITE_SCALING)

        self.ans_sprite1 = ModelSprite("images/ansbox.png", model=self.world.box1)
        self.ans_sprite2 = ModelSprite("images/ansbox.png", model=self.world.box2)
        self.ans_sprite3 = ModelSprite("images/ansbox.png", model=self.world.box3)
        self.ans_sprite4 = ModelSprite("images/ansbox.png", model=self.world.box4)
        self.ans_sprite5 = ModelSprite("images/ansbox.png", model=self.world.box5)
        self.ans_sprite6 = ModelSprite("images/ansbox.png", model=self.world.box6)

        self.ice_sprite = ModelSprite("images/ice.png", model=self.world.ice1)
        self.star_sprite = ModelSprite("images/star.png", model=self.world.star)
        self.time_sprite = ModelSprite("images/addtime.png", model=self.world.time)


        self.quiz_sprite1 = arcade.Sprite('images/nut.png')
        self.quiz_sprite1.center_x = 500
        self.quiz_sprite1.center_y = 700
        self.quiz_sprite2 = arcade.Sprite('images/bear.png')
        self.quiz_sprite2.center_x = 500
        self.quiz_sprite2.center_y = 700
        self.quiz_sprite3 = arcade.Sprite('images/prinny.png')
        self.quiz_sprite3.center_x = 500
        self.quiz_sprite3.center_y = 700
        self.quiz_sprite4 = arcade.Sprite('images/cat.png')
        self.quiz_sprite4.center_x = 500
        self.quiz_sprite4.center_y = 700

        self.choice1_sprite = arcade.Sprite('images/choice1.png',SPRITE_SCALING)
        self.choice1_sprite.center_x = 400
        self.choice1_sprite.center_y = 370
        self.choice2_sprite = arcade.Sprite('images/choice2.png', SPRITE_SCALING)
        self.choice2_sprite.center_x = 400
        self.choice2_sprite.center_y = 270
        self.choice3_sprite = arcade.Sprite('images/choice3.png', SPRITE_SCALING)
        self.choice3_sprite.center_x = 400
        self.choice3_sprite.center_y = 170

        self.p2_choice1_sprite = arcade.Sprite('images/choice1.png', SPRITE_SCALING)
        self.p2_choice1_sprite.center_x = 400
        self.p2_choice1_sprite.center_y = 370
        self.p2_choice2_sprite = arcade.Sprite('images/choice2.png', SPRITE_SCALING)
        self.p2_choice2_sprite.center_x = 400
        self.p2_choice2_sprite.center_y = 270
        self.p2_choice3_sprite = arcade.Sprite('images/choice3.png', SPRITE_SCALING)
        self.p2_choice3_sprite.center_x = 400
        self.p2_choice3_sprite.center_y = 170

        self.pointUFO_sprite = arcade.Sprite('images/pointufo.png', SPRITE_SCALING)
        self.pointUFO_sprite.center_x = 200
        self.pointUFO_sprite.center_y = 70
        self.pointSOM_sprite = arcade.Sprite('images/pointsom.png', SPRITE_SCALING)
        self.pointSOM_sprite.center_x = 800
        self.pointSOM_sprite.center_y = 70



    def setup(self):

        spaceword = 310
        order = 0
        self.play1lose_sprite.center_x = 442
        self.play1lose_sprite.center_y = 100
        self.play2lose_sprite.center_x = 552
        self.play2lose_sprite.center_y = 100

    def draw_instructions_page(self, page_number):
        page_texture = self.instructions[page_number]
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      page_texture.width,
                                      page_texture.height, page_texture, 0)

    def introgame(self):
        output = "Choose SOM or UFO"
        arcade.draw_text(output, 150, 800, arcade.color.BLACK_LEATHER_JACKET, 42)
        output = "SOM Control by: LEFT RIGHT UP DOWN"
        arcade.draw_text(output, 200, 730, arcade.color.PUMPKIN, 24)
        output = "UFO Control by: A D W S"
        arcade.draw_text(output, 200, 650, arcade.color.STRAWBERRY, 24)
        output = "How to play"
        arcade.draw_text(output, 200, 550, arcade.color.BLACK_LEATHER_JACKET, 24)
        output = "Collect the box in game to select choice"
        arcade.draw_text(output, 240, 450, arcade.color.BLUE_SAPPHIRE, 24)
        output = "1 Box == Choice 1 == 10 point"
        arcade.draw_text(output, 240, 390, arcade.color.BLUE_SAPPHIRE, 24)
        output = "Answer by enter on SHIFT"
        arcade.draw_text(output, 240, 330, arcade.color.BLUE_SAPPHIRE, 24)
        output = "In your turn, you must collect box to answer quiz"
        arcade.draw_text(output, 150, 180, arcade.color.RESOLUTION_BLUE, 24)
        output = "but another player can ้hinder you!? , Click to begin"
        arcade.draw_text(output, 150, 120, arcade.color.RED_ORANGE, 24)


    def draw_game(self):

        output = "ScoreSOM: {}".format(self.world.SCORE_TURN[0])
        arcade.draw_text(output, 40, 40, arcade.color.WHITE, 14)
        output = "ScoreUFO: {}".format(self.world.SCORE_TURN[1])
        arcade.draw_text(output, 850, 40, arcade.color.WHITE, 14)
        output = "POINT: {}".format(self.world.POINT_TURN[0])
        arcade.draw_text(output, 200, 40, arcade.color.WHITE, 14)
        output = "POINT: {}".format(self.world.POINT_TURN[1])
        arcade.draw_text(output, 750, 40, arcade.color.WHITE, 14)

    def draw_game_over(self):

        if self.world.POINT_TURN[0] > self.world.POINT_TURN[1]:
             output = "SOM WIN!!"
             arcade.draw_text(output, 430, 370, arcade.color.WHITE, 35)
             self.play2lose_sprite.draw()
        elif self.world.POINT_TURN[1] == self.world.POINT_TURN[0]:
             output = "YOU TWO LOSE"
             arcade.draw_text(output, 340, 370, arcade.color.WHITE, 35)
             self.play2_sprite.center_x = 552
             self.play2_sprite.center_y = 100
             self.play1lose_sprite.draw()
             self.play2lose_sprite.draw()
        else:
             output = "UFO WIN!!"
             arcade.draw_text(output, 430, 370, arcade.color.GREEN, 35)
             self.play1lose_sprite.draw()
        self.world.SCORE_TURN[0] = 0
        self.world.SCORE_TURN[1] = 0
    def on_draw(self):

        arcade.start_render()

        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.draw_instructions_page(0)
            output = "Click to start"
            arcade.draw_text(output, 310, 250, arcade.color.WHITE, 42)

        elif self.current_state == INSTRUCTIONS_PAGE_1:
            self.draw_instructions_page(3)
            self.introgame()

        elif self.current_state == GAME_RUNNING:
            self.draw_instructions_page(1)

            self.play1_sprite.draw()
            self.play2_sprite.draw()
            self.ans_sprite1.draw()
            self.ans_sprite2.draw()
            self.ans_sprite3.draw()
            self.ans_sprite4.draw()
            self.ans_sprite5.draw()
            self.ans_sprite6.draw()
            self.ice_sprite.draw()
            self.time_sprite.draw()
            self.star_sprite.draw()

            arcade.draw_text(self.world.OUTPUT, 750, 920, arcade.color.OCEAN_BOAT_BLUE, 30)

            if self.world.TURN == 0:
                output = "TURN "+self.Round[self.world.TURN]
                arcade.draw_text(output, 350+self.moveword, 550, arcade.color.CARROT_ORANGE, 20)
            if self.world.TURN == 1:
                output = "TURN " + self.Round[self.world.TURN]
                arcade.draw_text(output, 350 + self.moveword, 550, arcade.color.APPLE_GREEN, 20)

            output = "WHAT IS IT?"
            arcade.draw_text(output, 350 + self.moveword, 450, arcade.color.BLACK, 20)

            output = WORD[self.ORDER][0]
            arcade.draw_text(output, 450 , 350, arcade.color.BLACK, 30)
            output = WORD[self.ORDER][1]
            arcade.draw_text(output, 450 , 250, arcade.color.BLACK_OLIVE, 30)
            output = WORD[self.ORDER][2]
            arcade.draw_text(output, 450 , 150, arcade.color.BLACK_BEAN, 30)
            output = "SHIFT TO ANS"
            arcade.draw_text(output, 430, 100, arcade.color.WHITE, 15)

            if self.moveword >= 100:
                self.CASE = False
            if self.moveword <= 10:
                self.CASE = True
            if self.CASE:
                self.moveword += 1
            else:
                self.moveword -= 1

            if self.world.TIMEOUT <= 0:    #TIMER
                 self.current_state = GAME_OVER

            self.listquiz()
            self.checkscore()


        else:
            self.draw_instructions_page(2)
            self.draw_game_over()



    def listquiz(self):

        self.draw_game()

        if self.ORDER == 0:
            self.quiz_sprite1.draw()
        if self.ORDER == 1:
            self.quiz_sprite2.draw()
        if self.ORDER == 2:
            self.quiz_sprite3.draw()
        if self.ORDER == 3:
            self.quiz_sprite4.draw()

    def clean(self):
        for a in self.ans_list:
            a.kill()
        for a in self.ice_list:
            a.kill()
        for a in self.time_list:
            a.kill()

    def checkscore(self):

        if self.world.SCORE_TURN[0] >= 10:
            self.choice1_sprite.draw()
            self.Choice_som = 0
        if self.world.SCORE_TURN[0] >= 20:
            self.choice2_sprite.draw()
            self.Choice_som = 1
        if self.world.SCORE_TURN[0] >= 30:
            self.choice3_sprite.draw()
            self.Choice_som = 2
        if self.world.SCORE_TURN[1] >= 10:
            self.p2_choice1_sprite.draw()
            self.Choice_ufo = 0
        if self.world.SCORE_TURN[1] >= 20:
            self.p2_choice2_sprite.draw()
            self.Choice_ufo = 1
        if self.world.SCORE_TURN[1] >= 30:
            self.p2_choice3_sprite.draw()
            self.Choice_ufo = 2

        if self.checkans == 1:
            if self.Choice_som == NUMSTATUS[self.ORDER]:
                self.world.POINT_TURN[0] += 10
                self.ORDER += 1
                self.world.SCORE_TURN[0] = 0
                self.world.SCORE_TURN[1] = 0

                if self.world.TURN == 0:
                    self.world.TURN += 1
                else:
                    self.world.TURN -= 1
            else:
                self.checkans = 0
                self.world.SCORE_TURN[0] = 0

        if self.checkans == 2:
            if self.Choice_ufo == NUMSTATUS[self.ORDER]:
                self.world.POINT_TURN[1] += 10
                self.ORDER += 1
                self.world.SCORE_TURN[0] = 0
                self.world.SCORE_TURN[1] = 0
                if self.world.TURN == 0:
                    self.world.TURN += 1
                else:
                    self.world.TURN -= 1
            else:
                self.checkans = 0
                self.world.SCORE_TURN[1] = 0


    def on_mouse_press(self, x, y, button, modifiers):
        if self.current_state == INSTRUCTIONS_PAGE_0:
            # Next page of instructions.
            self.current_state = INSTRUCTIONS_PAGE_1
        elif self.current_state == INSTRUCTIONS_PAGE_1:
            # Start the game
            self.setup()
            self.current_state = GAME_RUNNING
        elif self.current_state == GAME_OVER:
            # Restart the game.
            self.setup()
            self.current_state = GAME_RUNNING

    def animate(self, delta):
        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.world.animate_start(delta)
        if self.current_state == GAME_RUNNING:

            self.world.setdirection()
            self.world.animate(delta)

        if self.current_state == INSTRUCTIONS_PAGE_1:
            self.world.animate_start(delta)
        if self.current_state == GAME_OVER:
            self.world.animate_end(delta)


    def on_key_press(self, key, key_modifiers):

       self.world.on_key_press(key, key_modifiers)
       if key == arcade.key.RSHIFT:
             self.checkans = 1
       if key == arcade.key.LSHIFT:
             self.checkans = 2


if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()