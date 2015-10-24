
import random
import json
import os
import sys
sys.path.append('../LabsAll/Labs')

from pico2d import *

import game_framework
import main_state
import main_state3

class Ground:
    def __init__(self):
        self.image = load_image('playground.png')

    def draw(self):
        self.image.clip_draw(0,0,600,751,400,430)

class Audience1:
    def __init__(self):
        self.image = load_image('audience1.png')

    def draw(self):
        self.image.clip_draw(0,0,165,751,50,430)

class Audience2:
    def __init__(self):
        self.image = load_image('audience2.png')

    def draw(self):
        self.image.clip_draw(0,0,165,751,750,430)

class Ball:
    def __init__(self):
        self.image = load_image('SoccerBall.png')

    def draw(self):
        self.image.clip_draw(0,0,50,48,400,430)

class User:
    def __init__(self):
        self.image = load_image('User.png')

    def draw(self):
        self.image.clip_draw(0, 0, 100, 112, x, y)

class Ai2:
    def __init__(self):
        self.image = load_image('AI2.png')

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
            x,y = event.x,800-event.y
        elif event.type == SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
             game_framework.change_state(main_state3)


ground=None
audience1=None
audience2=None
user=None
ball=None
ai2=None
running=True
x, y = 100, 100
hide_cursor()

def enter():
    global ground,audience1,audience2,user,ball,ai2
    open_canvas(800,800)
    user=User()
    ground=Ground()
    audience1=Audience1()
    audience2=Audience2()
    ball=Ball()
    ai2=Ai2()

def exit():
    global ground,audience1,audience2,user,ball,ai2
    del(ground)
    del(audience1)
    del(audience2)
    del(user)
    del(ball)
    del(ai2)
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
    ai2.draw()
    update_canvas()

def main():
    enter()
    while running:
        handle_events()
        update()
        draw()
    exit()

if __name__=='__main__':
    main()
