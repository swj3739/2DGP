import random

from pico2d import *

class Ball:
    PIXEL_PER_METER = (10.0 / 0.3) # 10 PIXEL 30cm
    RUN_SPEED_KMPH = 25.0          # Km / Hour 공속도조절
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS *  PIXEL_PER_METER) #초당 몇 픽셀?

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    image = None;


    def __init__(self):
        self.x , self.y = 400, 200
        self.frame = 7
        self.run_frames = 0
        self.distance = 0
        if Ball.image == None:
             Ball.image = load_image('resource/etc/SoccerBall.png')


    def update(self, frame_time):
        self.frame = (self.frame + 1) % 1
        self.y += self.distance
        if self.y > 770 or self.y < 90:
            self.y=200
            self.distance = 0



    def draw(self):
        self.image.clip_draw(0,0,50,48,self.x, self.y)


    def get_bb(self):
        return self.x - 20, self. y - 20, self. x + 20, self.y + 20


    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def moveball_up(self,frame_time):
        self.distance = Ball.RUN_SPEED_PPS * frame_time


    def moveball_down(self,frame_time):
        self.distance = Ball.RUN_SPEED_PPS * frame_time*(-1)



