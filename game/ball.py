import random

from pico2d import *

class Ball:

    image = None;


    def __init__(self):
        self.image = load_image('resource/etc/SoccerBall.png')

    def draw(self):
        self.image.clip_draw(0,0,50,48,400,200)
