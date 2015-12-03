import random
import json
import os
import sys
sys.path.append('../LabsAll/Labs')
import game_framework
import main_state3
from pico2d import *



from ball import Ball
time = 0


class Ai3:

    PIXEL_PER_METER = (10.0 / 0.3) # 10 PIXEL 30cm
    RUN_SPEED_KMPH = 50.0          # Km / Hour 캐릭터속도조절가능
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS *  PIXEL_PER_METER) #초당 몇 픽셀?

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    image = None;

    LEFT_RUN, RIGHT_RUN= 0, 1

    def handle_left_run(self):
        self.x -= self.distance
        self.run_frames += 1
        if self.x < 150:
            self.state = self.RIGHT_RUN
            self.x = 150
        if self.x < ball.x:
            self.state = self.RIGHT_RUN
            self.x = ball.x



    def handle_right_run(self):
        self.x += self.distance
        self.run_frames += 1
        if self.x > 650:
            self.state = self.LEFT_RUN
            self.x = 650
        if self.x > ball.x:
            self.state = self.LEFT_RUN
            self.x = ball.x





    handle_state = {
                LEFT_RUN: handle_left_run,
                RIGHT_RUN: handle_right_run,

    }



    def update(self,frame_time):
        self.distance = Ai3.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 1
        self.handle_state[self.state](self)


    def __init__(self):
        self.x, self.y = 300,750
        self.frame = 7
        self.run_frames = 0
        self.distance = 0
        self.state = self.RIGHT_RUN
        if Ai3.image == None:
            Ai3.image = load_image('resource/character/AI3.png')


    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 0, 100, 100, self.x, self.y)


    def get_up(self):
        return self.x - 10, self.y, self.x  + 10, self.y + 40


    def get_down(self):
        return self.x - 5, self.y - 40, self.x  + 5, self.y


    def get_right(self):
        return self.x, self.y - 10, self.x  + 30, self.y + 10


    def get_left(self):
        return self.x - 30, self.y - 10, self.x , self.y + 10


    def get_up_right(self):
        return self.x, self.y, self.x  + 25, self.y + 30


    def get_up_left(self):
        return self.x -25, self.y, self.x, self.y + 30


    def get_down_left(self):
        return self.x -25, self.y-30, self.x, self.y


    def get_down_right(self):
        return self.x, self.y-30, self.x+25, self.y


    def draw_bb(self):
        draw_rectangle(*self.get_up())
        draw_rectangle(*self.get_down())
        draw_rectangle(*self.get_right())
        draw_rectangle(*self.get_left ())
        draw_rectangle(*self.get_up_right())
        draw_rectangle(*self.get_up_left())
        draw_rectangle(*self.get_down_left())
        draw_rectangle(*self.get_down_right())


class Ground:

    image = None;

    def __init__(self):
        if Ground.image == None:
            Ground.image = load_image('resource/background/playground.png')
        self.x,self.y = 400,400


    def draw(self):

        self.image.clip_draw(0,0,600,751,400,430)



    def get_bb(self):


        return self.x - 400, self.y - 310, self.x  + 400, self.y + 370


    def draw_bb(self):


        draw_rectangle(*self.get_bb())


class Audience1:
    def __init__(self):
        self.image = load_image('resource/background/audience1.png')

    def draw(self):
        self.image.clip_draw(0,0,165,751,50,430)


class Audience2:
    def __init__(self):
        self.image = load_image('resource/background/audience2.png')

    def draw(self):
        self.image.clip_draw(0,0,165,751,750,430)


class ScoreBoard:


    image = None;


    def __init__(self):
        if ScoreBoard.image == None:
            ScoreBoard.image = load_image('resource/etc/ScoreBoard.png')

    def draw(self):
        self.image.clip_draw(0,0,800,70,400,20)


class Number_Me:


    image = None;


    def __init__(self):
        if Number_Me.image == None:
            Number_Me.image = load_image('resource/etc/Number.png')
        self.frame = 0


    def update(self):
        if ball.count_user == 1:
             self.frame = self.frame + 1
             ball.count_user = 0




    def draw(self):
        self.image.clip_draw(self.frame*23, 0,23, 76, 200, 30)


class Number_Ai:


    image = None;


    def __init__(self):
        if Number_Ai.image == None:
            Number_Ai.image = load_image('resource/etc/Number.png')
        self.frame = 0


    def update(self):
        if ball.count_ai == 1:
             self.frame = self.frame + 1
             ball.count_ai = 0




    def draw(self):
        self.image.clip_draw(self.frame*23, 0,23, 76, 600, 30)


class Win:


    image = None;


    def __init__(self):
        if Win.image == None:
            Win.image = load_image('resource/etc/Win.png')

    def draw(self):
        self.image.clip_draw(0,0,309,84,450,400)


class Lose:


    image = None;


    def __init__(self):
        if Lose.image == None:
            Lose.image = load_image('resource/etc/Lose.png')

    def draw(self):
        self.image.clip_draw(0,0,309,84,400,400)


class GameStart:


    image = None;


    def __init__(self):
        if GameStart.image == None:
            GameStart.image = load_image('resource/etc/GameStart.png')
        self.x = 400
    def update(self):
        if current_time > 4:
            self.x = 1000


    def draw(self):
        self.image.clip_draw(0,0,346,140,self.x,400)


class User:


    image = None;

    def __init__(self):

        if User.image == None:
            User.image = load_image('resource/character/User.png')

    def get_up(self):
        return self.x - 10, self.y, self.x  + 10, self.y + 40


    def get_down(self):
        return self.x - 10, self.y - 40, self.x  + 10, self.y


    def get_right(self):
        return self.x, self.y - 10, self.x  + 30, self.y + 10


    def get_left(self):
        return self.x - 30, self.y - 10, self.x , self.y + 10


    def get_up_right(self):
        return self.x, self.y, self.x  + 25, self.y + 30


    def get_up_left(self):
        return self.x -25, self.y, self.x, self.y + 30


    def get_down_left(self):
        return self.x -25, self.y-30, self.x, self.y


    def get_down_right(self):
        return self.x, self.y-30, self.x+25, self.y


    def update(self,frame_time):
        self.x, self.y = x, y


    def draw_bb(self):
        draw_rectangle(*self.get_up())
        draw_rectangle(*self.get_down())
        draw_rectangle(*self.get_right())
        draw_rectangle(*self.get_left ())
        draw_rectangle(*self.get_up_right())
        draw_rectangle(*self.get_up_left())
        draw_rectangle(*self.get_down_left())
        draw_rectangle(*self.get_down_right())


    def draw(self):
        self.image.clip_draw(0, 0, 100, 112,self.x,self.y)
        print(current_time)


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            if( x < 150 ):
                x,y = 149,800-event.y
                if( event.x >= 150 ):

                    x=150

            elif( x > 650 ):
                x,y = 651, 800-event.y
                if( event.x <= 650):

                    x = 650
            elif(x >= 150 and x <= 650):
                x,y = event.x,800-event.y


            if(y > 390):
                x,y = event.x,390
                if(x < 150):
                    x = 149
                elif( x> 650 ):
                    x = 651
            elif(y < 100 ):
                 x,y = event.x,100
                 if ( x <150):
                    x = 149
                 elif( x > 650):
                    x = 651


        elif event.type == SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            game_framework.quit()
        #elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
           #  game_framework.push_state(main_state3)


def collide_up(a, b):
   left_a, bottom_a, right_a, top_a = a.get_up()
   left_b, bottom_b, right_b, top_b = b.get_bb()
   #self.x - 30, self.y - 40, self.x  + 30, self.y + 40
   #self.x - 20, self. y - 20, self. x + 20, self.y + 20
   if left_a > right_b: return False
   if right_a < left_b: return False
   if top_a < bottom_b: return False
   if bottom_a > top_b: return False
   return True


def collide_down(a, b):
   left_a, bottom_a, right_a, top_a = a.get_down()
   left_b, bottom_b, right_b, top_b = b.get_bb()
   #self.x - 30, self.y - 40, self.x  + 30, self.y + 40
   #self.x - 20, self. y - 20, self. x + 20, self.y + 20
   if left_a > right_b: return False
   if right_a < left_b: return False
   if top_a < bottom_b: return False
   if bottom_a > top_b: return False
   return True


def collide_right(a, b):
   left_a, bottom_a, right_a, top_a = a.get_right()
   left_b, bottom_b, right_b, top_b = b.get_bb()

   if left_a > right_b: return False
   if right_a < left_b: return False
   if top_a <bottom_b: return False
   if bottom_a > top_b: return False
   return True


def collide_left(a, b):
   left_a, bottom_a, right_a, top_a = a.get_left()
   left_b, bottom_b, right_b, top_b = b.get_bb()

   if left_a > right_b: return False
   if right_a < left_b: return False
   if top_a <bottom_b: return False
   if bottom_a > top_b: return False
   return True


def collide_up_right(a, b):
   left_a, bottom_a, right_a, top_a = a.get_up_right()
   left_b, bottom_b, right_b, top_b = b.get_bb()

   if left_a > right_b: return False
   if right_a < left_b: return False
   if top_a <bottom_b: return False
   if bottom_a > top_b: return False
   return True


def collide_up_left(a, b):
   left_a, bottom_a, right_a, top_a = a.get_up_left()
   left_b, bottom_b, right_b, top_b = b.get_bb()

   if left_a > right_b: return False
   if right_a < left_b: return False
   if top_a <bottom_b: return False
   if bottom_a > top_b: return False
   return True


def collide_down_left(a, b):
   left_a, bottom_a, right_a, top_a = a.get_down_left()
   left_b, bottom_b, right_b, top_b = b.get_bb()

   if left_a > right_b: return False
   if right_a < left_b: return False
   if top_a <bottom_b: return False
   if bottom_a > top_b: return False
   return True


def collide_down_right(a, b):
   left_a, bottom_a, right_a, top_a = a.get_down_right()
   left_b, bottom_b, right_b, top_b = b.get_bb()

   if left_a > right_b: return False
   if right_a < left_b: return False
   if top_a <bottom_b: return False
   if bottom_a > top_b: return False
   return True

win = None
lose = None
ground=None
scoreboard=None
number_me = None
number_ai = None
audience1=None
audience2=None
running=True
gamestart = None
current_time = get_time()
x, y = 100, 100
hide_cursor()


def enter():
    global ground,audience1,audience2,user,ball,ai3,scoreboard,number_me,number_ai,win,lose,gamestart
    open_canvas(800,800,sync = True)
    user=User()
    ground=Ground()
    audience1 = Audience1()
    audience2 = Audience2()
    scoreboard = ScoreBoard()
    ball = Ball()
    ai3 = Ai3()
    win = Win()
    lose = Lose()
    number_me = Number_Me()
    number_ai = Number_Ai()
    gamestart = GameStart()


def exit():
    global ground,audience1,audience2,user,ball,ai3,scoreboard,number_me,number_ai,win,lose,gamestart
    del(ground)
    del(audience1)
    del(audience2)
    del(user)
    del(ball)
    del(ai3)
    del(scoreboard)
    del(number_me)
    del(number_ai)
    del(gamestart)
    close_canvas()

def get_frame_time():

    global current_time
    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def update():
     global time
     time = get_frame_time()
     ai3.update(time)
     ball.update(time)
     user.update(time)
     number_me.update()
     number_ai.update()
     gamestart.update()
     if collide_up(user,ball):#유저와 볼 충돌
         ball.moveball_up(time)
     if collide_down(user,ball):
         ball.moveball_down(time)
     if collide_right(user,ball):
         ball.moveball_right(time)
     if collide_left(user,ball):
         ball.moveball_left(time)
     if collide_up_right(user,ball):
         ball.moveball_up_right(time)
     if collide_up_left(user,ball):
         ball.moveball_up_left(time)
     if collide_down_left(user,ball):
         ball.moveball_down_left(time)
     if collide_down_right (user,ball):
         ball.moveball_down_right(time)

     if collide_up(ai3,ball):#ai와 볼충돌
         ball.moveball_up(time)
     if collide_down(ai3,ball):
         ball.moveball_down(time)
     if collide_right(ai3,ball):
         ball.moveball_right(time)
     if collide_left(ai3,ball):
         ball.moveball_left(time)
     if collide_up_right(ai3,ball):
         ball.moveball_up_right(time)
     if collide_up_left(ai3,ball):
         ball.moveball_up_left(time)
     if collide_down_left(ai3,ball):
         ball.moveball_down_left(time)
     if collide_down_right (ai3,ball):
         ball.moveball_down_right(time)





def draw():
    clear_canvas()
    ground.draw()
    user.draw()
    audience1.draw()
    audience2.draw()
    scoreboard.draw()
    number_me.draw()
    number_ai.draw()
    ball.draw()
    ai3.draw()
    user.draw_bb()
    ball.draw_bb()
    ai3.draw_bb()
    gamestart.draw()
    if number_me.frame >= 5:
        win.draw()
    if number_ai.frame >= 5:
        lose.draw()
    ground.draw_bb()
    update_canvas()


def pause():
    pass


def resume():
    pass

