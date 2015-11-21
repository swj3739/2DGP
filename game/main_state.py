import random
import json
import os
import sys
sys.path.append('../LabsAll/Labs')
import game_framework
import main_state2
from pico2d import *


from ai1 import Ai1
from ball import Ball
time = 0

class Ground:

    image = None;

    def __init__(self):
        if Ground.image == None:
            Ground.image = load_image('resource/background/playground.png')
        self.x,self.y=400,400

    def draw(self):

        self.image.clip_draw(0,0,600,751,400,430)



    def get_bb(self):
        return self.x - 265, self.y - 310, self.x  + 265, self.y + 370


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

class User:

    image = None;

    def __init__(self):

        if User.image == None:
            User.image = load_image('resource/character/User.png')

    def get_bb(self):
        return self.x - 30, self.y - 40, self.x  + 30, self.y + 40

    def update(self,frame_time):
        self.x, self.y = x, y


    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def draw(self):
        self.image.clip_draw(0, 0, 100, 112,self.x,self.y)
        print(self.x ,self.y)


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

                    x = 651
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
           #  game_framework.push_state(main_state2)


def collide(a, b):
   left_a, bottom_a, right_a, top_a = a.get_bb()
   left_b, bottom_b, right_b, top_b = b.get_bb()

   if left_a > right_b: return False
   if right_a < left_b: return False
   if top_a < bottom_b: return False
   if bottom_a > top_b: return False
   return True

def collide_ground(a, b):
   left_a, bottom_a, right_a, top_a = a.get_bb()
   left_b, bottom_b, right_b, top_b = b.get_bb()

   if left_a < right_b: return False
   if right_a > left_b: return False
   if top_a <bottom_b: return False
   if bottom_a > top_b: return False
   return True


ground=None
audience1=None
audience2=None
running=True
current_time = get_time()
x, y = 100, 100
hide_cursor()


def enter():
    global ground,audience1,audience2,user,ball,ai1
    open_canvas(800,800)
    user=User()
    ground=Ground()
    audience1=Audience1()
    audience2=Audience2()
    ball=Ball()
    ai1=Ai1()


def exit():
    global ground,audience1,audience2,user,ball,ai1
    del(ground)
    del(audience1)
    del(audience2)
    del(user)
    del(ball)
    del(ai1)
    close_canvas()

def get_frame_time():

    global current_time
    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def update():
     global time
     time = get_frame_time()
     ai1.update(time)
     ball.update(time)
     user.update(time)

     if collide(user,ball):
         ball.moveball_up(time)


     if collide(ai1,ball):
         ball.moveball_down(time)




def draw():
    clear_canvas()
    ground.draw()
    user.draw()
    audience1.draw()
    audience2.draw()
    ball.draw()
    ai1.draw()
    user.draw_bb()
    ball.draw_bb()
    ai1.draw_bb()
    ground.draw_bb()
    update_canvas()


def pause():
    pass


def resume():
    pass

