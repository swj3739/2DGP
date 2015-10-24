import random
import json
import os
import sys
sys.path.append('../LabsAll/Labs')

from pico2d import *

import game_framework
import title_state

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running == False
        elif event.type == SDL_MOUSEMOTION:
            x,y = event.x,800-event.y
        elif event.type == SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            running =False



open_canvas(800,800)
ground=load_image('playground.png')
audience1=load_image('audience1.png')
audience2=load_image('audience2.png')
ball=load_image('SoccerBall.png')
user=load_image('User.png')
ai1=load_image('AI1.png')


running = True
x, y = 100, 100

hide_cursor()

while (running):
    clear_canvas()
    ground.clip_draw(0,0,600,751,400,430)
    user.clip_draw(0, 0, 100, 112, x, y)
    audience1.clip_draw(0,0,165,751,50,430)
    audience2.clip_draw(0,0,165,751,750,430)
    ball.clip_draw(0,0,50,48,400,430)
    ai1.clip_draw(0,0,100,100,400,750)



    delay(0.001)
    handle_events()
    update_canvas()

close_canvas()