import random
import json
import os
import sys
sys.path.append('../LabsAll/Labs')
import game_framework
import round_3
import lose_screen
from pico2d import *


from ball import Ball
time = 0


class Ai2:

    PIXEL_PER_METER = (10.0 / 0.3) # 10 PIXEL 30cm
    RUN_SPEED_KMPH = 130.0         # Km / Hour 캐릭터속도조절가능
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS *  PIXEL_PER_METER) #초당 몇 픽셀?

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8


    LEFT_RUN, RIGHT_RUN= 0, 1

    def handle_left_run(self):
        self.x -= self.distance
        self.run_frames += 1
        if self.x < 150:
            self.state = self.RIGHT_RUN
            self.x = 150


    def handle_right_run(self):
        self.x += self.distance
        self.run_frames += 1
        if self.x > 650:
            self.state = self.LEFT_RUN
            self.x = 650


    handle_state = {
                LEFT_RUN: handle_left_run,
                RIGHT_RUN: handle_right_run,

    }



    def update(self,frame_time):
        self.distance = Ai2.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 1
        self.handle_state[self.state](self)


    def __init__(self):
        self.x, self.y = 300,750
        self.frame = 7
        self.run_frames = 0
        self.distance = 0
        self.state = self.RIGHT_RUN
        self.image = load_image('resource/character/AI2.png')


    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 0, 100, 100, self.x, self.y)


    def get_up(self):
        return self.x - 15, self.y, self.x  + 15, self.y + 40


    def get_down(self):
        return self.x - 15, self.y - 50, self.x  +15, self.y


    def get_right(self):
        return self.x, self.y - 10, self.x  + 45, self.y + 10


    def get_left(self):
        return self.x - 45, self.y - 10, self.x , self.y + 10


    def get_up_right(self):
        return self.x, self.y, self.x  + 25, self.y + 30


    def get_up_left(self):
        return self.x -25, self.y, self.x, self.y + 30


    def get_down_left(self):
        return self.x -35, self.y-40, self.x, self.y


    def get_down_right(self):
        return self.x, self.y-40, self.x+35, self.y


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


    def __init__(self):
        self.image = load_image('resource/background/playground.png')
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


    def __init__(self):
        self.image = load_image('resource/etc/ScoreBoard.png')

    def draw(self):
        self.image.clip_draw(0,0,800,70,400,20)


class Number_Me:

    def __init__(self):
        self.image = load_image('resource/etc/Number.png')
        self.frame = 0
        self.end_time = 0


    def update(self):
        if ball.count_user == 1:
             self.frame = self.frame + 1
             ball.count_user = 0
             if self.frame >= 5:
                 self.end_time = current_time





    def draw(self):
        self.image.clip_draw(self.frame*23, 0,23, 76, 200, 30)
        print(self. end_time)


class Number_Ai:

    def __init__(self):
        self.image = load_image('resource/etc/Number.png')
        self.frame = 0
        self.end_time = 0


    def update(self):
        if ball.count_ai == 1:
             self.frame = self.frame + 1
             ball.count_ai = 0
             if self.frame >= 5:
                  self.end_time = current_time




    def draw(self):
        self.image.clip_draw(self.frame*23, 0,23, 76, 600, 30)


class Win:




    def __init__(self):
        self.image = load_image('resource/etc/Win.png')

    def draw(self):
        self.image.clip_draw(0,0,309,84,450,400)


class Lose:

    sound = None

    def __init__(self):
        self.image = load_image('resource/etc/Lose.png')
        if Lose.sound == None:
            Lose.sound = load_wav('sound/lose.wav')
            Lose.sound.set_volume(32)

    def draw(self):
        self.image.clip_draw(0,0,309,84,400,400)




class GameStart:


    def __init__(self):
        self.image = load_image('resource/etc/GameStart.png')
        self.x = 400
    def update(self):
        if current_time > 4:
            self.x = 1000


    def draw(self):
        self.image.clip_draw(0,0,346,140,self.x,400)


class User:


    def __init__(self):

        self.image = load_image('resource/character/User.png')

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
        if number_me.frame >= 5:
             if current_time - number_me.end_time > 5:
                game_framework.push_state(round_3)


        if number_ai.frame >= 5:
            if current_time - number_ai.end_time > 5:
                Lose.sound.play()
                game_framework.change_state(lose_screen)


def collide_up(a, b):
   left_a, bottom_a, right_a, top_a = a.get_up()
   left_b, bottom_b, right_b, top_b = b.get_bb()


   if left_a > right_b: return False
   if right_a < left_b: return False
   if top_a < bottom_b: return False
   if bottom_a > top_b: return False
   return True


def collide_down(a, b):
   left_a, bottom_a, right_a, top_a = a.get_down()
   left_b, bottom_b, right_b, top_b = b.get_bb()


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
    global ground,audience1,audience2,user,ball,ai2,scoreboard,number_me,number_ai,win,lose,gamestart
    user=User()
    ground=Ground()
    audience1 = Audience1()
    audience2 = Audience2()
    scoreboard = ScoreBoard()
    ball = Ball()
    ai2 = Ai2()
    win = Win()
    lose = Lose()
    number_me = Number_Me()
    number_ai = Number_Ai()
    gamestart = GameStart()


def exit():
    global ground,audience1,audience2,user,ball,ai2,scoreboard,number_me,number_ai,win,lose,gamestart
    del(ground)
    del(audience1)
    del(audience2)
    del(user)
    del(ball)
    del(ai2)
    del(scoreboard)
    del(number_me)
    del(number_ai)
    del(gamestart)


def get_frame_time():

    global current_time
    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def update():
     global time
     time = get_frame_time()
     ai2.update(time)
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

     if collide_up(ai2,ball):#ai와 볼충돌
         ball.moveball_up(time)
     if collide_down(ai2,ball):
         ball.moveball_down(time)
     if collide_right(ai2,ball):
         ball.moveball_right(time)
     if collide_left(ai2,ball):
         ball.moveball_left(time)
     if collide_up_right(ai2,ball):
         ball.moveball_up_right(time)
     if collide_up_left(ai2,ball):
         ball.moveball_up_left(time)
     if collide_down_left(ai2,ball):
         ball.moveball_down_left(time)
     if collide_down_right (ai2,ball):
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
    ai2.draw()
    user.draw_bb()
    ball.draw_bb()
    ai2.draw_bb()
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

