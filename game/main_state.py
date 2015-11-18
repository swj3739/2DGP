import random
import json
import os
import sys
sys.path.append('../LabsAll/Labs')
import game_framework
import main_state2
from pico2d import *

from ball import Ball
from ai1 import Ai1

class Ground:
    def __init__(self):
        self.image = load_image('resource/background/playground.png')

    def draw(self):
        self.image.clip_draw(0,0,600,751,400,430)


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


    def draw(self):
        self.image.clip_draw(0, 0, 100, 112,x, y)


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
                    x = 650
            elif(y < 100 ):
                 x,y = event.x,100
                 if ( x <150):
                    x = 149
                 elif( x > 650):
                    x = 650


        elif event.type == SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
             game_framework.push_state(main_state2)


ground=None
audience1=None
audience2=None
running=True
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


def update():
     ai1.update()


def draw():
    clear_canvas()
    ground.draw()
    user.draw()
    audience1.draw()
    audience2.draw()
    ball.draw()
    ai1.draw()
    update_canvas()


def pause():
    pass


def resume():
    pass

