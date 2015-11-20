import random

from pico2d import *

class Ball:

    image = None;


    def __init__(self):
        self.x , self.y = 400, 200
        if Ball.image == None:
             Ball.image = load_image('resource/etc/SoccerBall.png')


    def update(self, frame_time):
        pass


    def draw(self):
        self.image.clip_draw(0,0,50,48,self.x, self.y)


    def get_bb(self):
        return self.x - 10, self. y - 10, self. x + 10, self.y + 10
