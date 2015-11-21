import random


from pico2d import *


class Ai1:

    PIXEL_PER_METER = (10.0 / 0.3) # 10 PIXEL 30cm
    RUN_SPEED_KMPH = 30.0          # Km / Hour 캐릭터속도조절가능
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
        self.distance = Ai1.RUN_SPEED_PPS * frame_time
        self.frame = (self.frame + 1) % 1
        self.handle_state[self.state](self)


    def __init__(self):
        self.x, self.y = 300,750
        self.frame = 7
        self.run_frames = 0
        self.distance = 0
        self.state = self.RIGHT_RUN
        if Ai1.image == None:
            Ai1.image = load_image('resource/character/AI1.png')


    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 0, 100, 100, self.x, self.y)


    def get_bb(self):
        return self.x - 30, self.y - 40, self.x  + 30, self.y + 40


    def draw_bb(self):
        draw_rectangle(*self.get_bb())



