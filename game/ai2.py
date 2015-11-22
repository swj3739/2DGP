import random


from pico2d import *


class Ai2:

    PIXEL_PER_METER = (10.0 / 0.3) # 10 PIXEL 30cm
    RUN_SPEED_KMPH = 100.0         # Km / Hour 캐릭터속도조절가능
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
        if Ai2.image == None:
            Ai2.image = load_image('resource/character/AI2.png')


    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 0, 100, 100, self.x, self.y)


    def get_up(self):
        return self.x - 15, self.y, self.x  + 15, self.y + 40


    def get_down(self):
        return self.x - 15, self.y - 50, self.x  + 15, self.y


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