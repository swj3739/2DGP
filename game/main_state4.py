import random
import json
import os
import sys
sys.path.append('../LabsAll/Labs')

from pico2d import *

import game_framework
import main_state


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


class Ball:
    def __init__(self):
        self.image = load_image('resource/etc/SoccerBall.png')

    def draw(self):
        self.image.clip_draw(0,0,50,48,400,200)


class User:
    def __init__(self):
        self.image = load_image('resource/character/User.png')

    def draw(self):
        self.image.clip_draw(0, 0, 100, 112, x, y)


class Ai4:
    def __init__(self):
        self.image = load_image('resource/character/AI4.png')

    def draw(self):
        self.image.clip_draw(0,0,100,100,400,750)


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            if(x<150):
                x,y=149,800-event.y
                if(event.x>=150):

                    x=150

            elif(x>650):
                x,y=651,800-event.y
                if(event.x<=650):

                    x=650
            elif(x>=150 and x<=650):
                x,y = event.x,800-event.y


            if(y>390):
                x,y=event.x,390
                if(x<150):
                    x=149
                elif(x>650):
                    x=650
            elif(y<100):
                 x,y=event.x,100
                 if(x<150):
                    x=149
                 elif(x>650):
                    x=650


        elif event.type == SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            game_framework.quit()


ground=None
audience1=None
audience2=None
user=None
ball=None
ai4=None
running=True
x, y = 100, 100
hide_cursor()


def enter():
    global ground,audience1,audience2,user,ball,ai4
    user=User()
    ground=Ground()
    audience1=Audience1()
    audience2=Audience2()
    ball=Ball()
    ai4=Ai4()


def exit():
    global ground,audience1,audience2,user,ball,ai4
    del(ground)
    del(audience1)
    del(audience2)
    del(user)
    del(ball)
    del(ai4)
    close_canvas()


def update():
    pass


def draw():
    clear_canvas()
    ground.draw()
    user.draw()
    audience1.draw()
    audience2.draw()
    ball.draw()
    ai4.draw()
    update_canvas()


def pause():
    pass


def resume():
    pass
