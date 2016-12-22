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
    SCOREUFO = 0
    SCORESOM = 0
    SCORETURN = [SCORESOM,SCOREUFO]
    list =0
    Choice_som = -1
    Choice_ufo = -1
    ChoiceTRUN = [Choice_som,Choice_ufo]
    POINTSOM = 0
    POINTUFO = 0
    ORDER =0
    checkans =0
    TURN = 0
    TIMELIMIT = 60
    STOP =0
    TIMESLEEP =0

    def __init__(self, width, height):
        super().__init__(width, height)

        self.all_sprites_list = None
        self.wall_list = None
        self.ans_list = None
        self.physics_engine = None
        self.physics_engine1 = None

        arcade.set_background_color(arcade.color.AMAZON)

        self.current_state = INSTRUCTIONS_PAGE_0

        self.instructions = []
        texture = arcade.load_texture("images/start-bg.png")
        self.instructions.append(texture)

        texture = arcade.load_texture("images/running_bg.png")
        self.instructions.append(texture)

        texture = arcade.load_texture("images/end-bg.png")
        self.instructions.append(texture)

        self.world = World(width, height)

        self.play1_sprite = ModelSprite('images/SOM.png',SPRITE_SCALING, model=self.world.play1)
        self.play1lose_sprite = ModelSprite('images/SOMSAD.png',SPRITE_SCALING)
        self.play2_sprite = ModelSprite('images/UFO.png',SPRITE_SCALING,model=self.world.play2)
        self.play2lose_sprite = ModelSprite('images/UFOSAD.png', SPRITE_SCALING)

        self.box_sprite = ModelSprite('images/wall.png', model=self.world.box)

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
        self.choice1_sprite.center_x = 60
        self.choice1_sprite.center_y = 100
        self.choice2_sprite = arcade.Sprite('images/choice2.png', SPRITE_SCALING)
        self.choice2_sprite.center_x = 60
        self.choice2_sprite.center_y = 150
        self.choice3_sprite = arcade.Sprite('images/choice3.png', SPRITE_SCALING)
        self.choice3_sprite.center_x = 60
        self.choice3_sprite.center_y = 200

        self.p2_choice1_sprite = arcade.Sprite('images/choice1.png', SPRITE_SCALING)
        self.p2_choice1_sprite.center_x = 930
        self.p2_choice1_sprite.center_y = 100
        self.p2_choice2_sprite = arcade.Sprite('images/choice2.png', SPRITE_SCALING)
        self.p2_choice2_sprite.center_x = 930
        self.p2_choice2_sprite.center_y = 150
        self.p2_choice3_sprite = arcade.Sprite('images/choice3.png', SPRITE_SCALING)
        self.p2_choice3_sprite.center_x = 930
        self.p2_choice3_sprite.center_y = 200
        
        self.pointUFO_sprite = arcade.Sprite('images/pointufo.png', SPRITE_SCALING)
        self.pointUFO_sprite.center_x = 200
        self.pointUFO_sprite.center_y = 70
        self.pointSOM_sprite = arcade.Sprite('images/pointsom.png', SPRITE_SCALING)
        self.pointSOM_sprite.center_x = 800
        self.pointSOM_sprite.center_y = 70



    def setup(self):

        spaceword = 310
        order = 0

        self.total_time = 0.0
        self.all_sprites_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.ans_list = arcade.SpriteList()
        self.time_list = arcade.SpriteList()
        self.ice_list = arcade.SpriteList()


        self.play1_sprite.center_x = 400
        self.play1_sprite.center_y = 400
        self.play2_sprite.center_x = 900
        self.play2_sprite.center_y = 450

        self.play1lose_sprite.center_x = 442
        self.play1lose_sprite.center_y = 100
        self.play2lose_sprite.center_x = 552
        self.play2lose_sprite.center_y = 100

        self.all_sprites_list.append(self.play1_sprite)
        self.all_sprites_list.append(self.play2_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(self.play1_sprite,
                                                         self.wall_list)
        self.physics_engine1 = arcade.PhysicsEngineSimple(self.play2_sprite,
                                                         self.wall_list)

    def draw_instructions_page(self, page_number):
        page_texture = self.instructions[page_number]
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      page_texture.width,
                                      page_texture.height, page_texture, 0)

    def draw_game(self):

        output = "ScoreSOM: {}".format(self.SCORESOM)
        arcade.draw_text(output, 40, 40, arcade.color.WHITE, 14)
        output = "ScoreUFO: {}".format(self.SCOREUFO)
        arcade.draw_text(output, 850, 40, arcade.color.WHITE, 14)
        output = "POINT: {}".format(self.POINTSOM)
        arcade.draw_text(output, 200, 40, arcade.color.WHITE, 14)
        output = "POINT: {}".format(self.POINTUFO)
        arcade.draw_text(output, 750, 40, arcade.color.WHITE, 14)

    def draw_game_over(self):

        output = "Click to restart"
        arcade.draw_text(output, 400, 470, arcade.color.WHITE, 24)
        if self.POINTSOM > self.POINTUFO:
             output = "SOM WIN!!"
             arcade.draw_text(output, 430, 370, arcade.color.WHITE, 35)
             self.play1_sprite.center_x = 442
             self.play1_sprite.center_y = 400
             self.play2lose_sprite.draw()
        elif self.POINTUFO == self.POINTSOM:
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
        self.world.score = 0

    def on_draw(self):

        arcade.start_render()

        if self.current_state == INSTRUCTIONS_PAGE_0:
            self.draw_instructions_page(0)
            output = "Click to start"
            arcade.draw_text(output, 310, 250, arcade.color.WHITE, 42)

        elif self.current_state == INSTRUCTIONS_PAGE_1:
            output = "Please choose SOM, UFO"
            arcade.draw_text(output, 240, 700, arcade.color.WHITE_SMOKE, 42)
            output = "How to play"
            arcade.draw_text(output, 240, 600, arcade.color.WHITE_SMOKE, 32)
            output = "Collect char in game quiz to win"
            arcade.draw_text(output, 240, 500, arcade.color.WHITE_SMOKE, 32)

        elif self.current_state == GAME_RUNNING:
            self.draw_instructions_page(1)
            seconds = int(self.total_time) % 60

            output = "Time: {:02d}" .format(self.TIMELIMIT-seconds)
            a = int(format(self.TIMELIMIT-seconds))
            arcade.draw_text(output, 750, 920, arcade.color.OCEAN_BOAT_BLUE, 30)
            output = "WHAT IS IT?"
            arcade.draw_text(output, 350+self.moveword, 920, arcade.color.BLACK, 20)

            output = WORD[self.ORDER][0]
            arcade.draw_text(output, 550 + self.moveword, 450, arcade.color.BLACK, 20)
            output = WORD[self.ORDER][1]
            arcade.draw_text(output, 450 + self.moveword, 350, arcade.color.BLACK_OLIVE, 20)
            output = WORD[self.ORDER][2]
            arcade.draw_text(output, 350 + self.moveword, 250, arcade.color.BRIGHT_LAVENDER, 20)

            if self.moveword >= 100:
                self.CASE = False
            if self.moveword <= 10:
                self.CASE = True
            if self.CASE:
                self.moveword += 1
            else:
                self.moveword -= 1

            if a <= 1:    #TIMER
                self.current_state = GAME_OVER

            if self.TIMESET == int(seconds):
                for x in range(10):
                    ans = arcade.Sprite("images/ansbox.png", SPRITE_SCALING/2)

                    ans.center_x = random.randrange(SCREEN_WIDTH)
                    ans.center_y = random.randrange(SCREEN_HEIGHT)

                    self.all_sprites_list.append(ans)
                    self.ans_list.append(ans)
                if self.TIMESET%10 ==0:
                    for x in range(1):
                        ice = arcade.Sprite("images/ice.png", SPRITE_SCALING)
                        ice.center_x = random.randrange(SCREEN_WIDTH)
                        ice.center_y = random.randrange(SCREEN_HEIGHT)
                        self.all_sprites_list.append(ice)
                        self.ice_list.append(ice)
                if (self.TIMESET%15 == 0)and(self.TIMESET !=0):
                    for x in range(1):
                        atime = self.addtime_sprite
                        atime.center_x = random.randrange(SCREEN_WIDTH)
                        atime.center_y = random.randrange(SCREEN_HEIGHT)
                        self.all_sprites_list.append(atime)
                        self.time_list.append(atime)
                self.TIMESET += 5

            if self.STOP != 0:
                self.TIMESLEEP += 1

            if self.TIMESLEEP == 100:
                self.STOP =0
                self.TIMESLEEP = 0

            self.draw_game()
            self.all_sprites_list.draw()
            if self.ORDER == 0:
               self.quiz_sprite1.draw()
            if self.ORDER == 1:
                self.quiz_sprite2.draw()
            if self.ORDER == 2:
                self.quiz_sprite3.draw()
            if self.ORDER == 3:
                self.quiz_sprite4.draw()

            if self.SCORESOM >= 10:
               self.choice1_sprite.draw()
               self.Choice_som = 0
            if self.SCORESOM >= 20:
                self.choice2_sprite.draw()
                self.Choice_som = 1
            if self.SCORESOM >= 30:
                self.choice3_sprite.draw()
                self.Choice_som = 2
            if self.SCOREUFO >= 10:
                self.p2_choice1_sprite.draw()
                self.Choice_ufo = 0
            if self.SCOREUFO >= 20:
                self.p2_choice2_sprite.draw()
                self.Choice_ufo = 1
            if self.SCOREUFO >= 30:
                self.p2_choice3_sprite.draw()
                self.Choice_ufo = 2

            if self.checkans == 1:
                if self.Choice_som == NUMSTATUS[self.ORDER]:
                    self.POINTSOM += 10
                    self.ORDER += 1
                    self.SCORESOM =0
                    self.SCOREUFO =0

                    if self.TURN == 0:
                      self.TURN += 1
                    else:
                        self.TURN -= 1
                else:
                    self.checkans =0
                    self.SCORESOM =0

            if self.checkans == 2:
                if self.Choice_ufo == NUMSTATUS[self.ORDER]:
                    self.POINTUFO += 10
                    self.ORDER += 1
                    self.SCORESOM = 0
                    self.SCOREUFO = 0
                    if self.TURN == 0:
                       self.TURN += 1
                    else:
                        self.TURN -= 1
                else:
                    self.checkans =0
                    self.SCOREUFO =0


        else:
            self.draw_instructions_page(2)
            self.draw_game_over()




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
            self.total_time += delta
            self.world.setdirection()
            self.world.animate(delta)

        self.all_sprites_list.update()

        hit_list_box = \
            arcade.check_for_collision_with_list(self.play1_sprite,
                                                 self.ans_list)
        hit_list_timer = \
            arcade.check_for_collision_with_list(self.play1_sprite,
                                                 self.time_list)

        hit_list_ice = \
            arcade.check_for_collision_with_list(self.play1_sprite,
                                                 self.ice_list)

        for ans in hit_list_box:
            ans.kill()
            if self.TURN == 0:
             self.SCORESOM += 1
            else:
             self.SCOREUFO -= 1

        for time in hit_list_timer:
            time.kill()
            self.TIMELIMIT += 10

        for ice in hit_list_ice:
            ice.kill()
            self.STOP =2


        hit_list1_box = \
            arcade.check_for_collision_with_list(self.play2_sprite,
                                                 self.ans_list)

        hit_list1_timer = \
            arcade.check_for_collision_with_list(self.play2_sprite,
                                                 self.time_list)

        hit_list1_ice = \
            arcade.check_for_collision_with_list(self.play2_sprite,
                                                 self.ice_list)

        for ans in hit_list1_box:
            ans.kill()
            if self.TURN == 1:
                self.SCOREUFO += 1
            else:
                self.SCORESOM -= 1


        for time in hit_list1_timer:
            time.kill()
            self.TIMELIMIT += 10

        for ice in hit_list1_ice:
            ice.kill()
            self.STOP = 1


        if self.current_state == INSTRUCTIONS_PAGE_1:
            self.world.animate_start(delta)
        if self.current_state == GAME_OVER:
            self.world.animate_end(delta)

        self.physics_engine.update()
        self.physics_engine1.update()



    def on_key_press(self, key, key_modifiers):

       if self.STOP != 1:
          if key == arcade.key.UP:
             self.play1_sprite.change_y = 5
          elif key == arcade.key.DOWN:
             self.play1_sprite.change_y = -5
          elif key == arcade.key.LEFT:
             self.play1_sprite.change_x = -5
          elif key == arcade.key.RIGHT:
             self.play1_sprite.change_x = 5
          elif key == arcade.key.RSHIFT:
             self.checkans = 1

       if self.STOP != 2:
          if key == arcade.key.W:
              self.play2_sprite.change_y = 5
          elif key == arcade.key.S:
              self.play2_sprite.change_y = -5
          elif key == arcade.key.A:
              self.play2_sprite.change_x = -5
          elif key == arcade.key.D:
              self.play2_sprite.change_x = 5
          elif key == arcade.key.LSHIFT:
              self.checkans = 2

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.play1_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.play1_sprite.change_x = 0

        if key == arcade.key.W or key == arcade.key.S:
            self.play2_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.play2_sprite.change_x = 0




if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()