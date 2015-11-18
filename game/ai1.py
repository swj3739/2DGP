import random


from pico2d import *


class Ai1:

    image = None;

    LEFT_RUN, RIGHT_RUN= 0, 1

    def handle_left_run(self):
        self.x -= 5
        self.run_frames += 1
        if self.x < 150:
            self.state = self.RIGHT_RUN
            self.x = 150


    def handle_right_run(self):
        self.x += 5
        self.run_frames += 1
        if self.x > 650:
            self.state = self.LEFT_RUN
            self.x = 650


    handle_state = {
                LEFT_RUN: handle_left_run,
                RIGHT_RUN: handle_right_run,

    }


    def update(self):
        self.frame = (self.frame + 1) % 1
        self.handle_state[self.state](self)


    def __init__(self):
        self.x, self.y = 300,750
        self.frame = 7
        self.run_frames = 0
        self.state = self.RIGHT_RUN
        if Ai1.image == None:
            Ai1.image = load_image('resource/character/AI1.png')


    def draw(self):
        self.image.clip_draw(self.frame * 100, self.state * 0, 100, 100, self.x, self.y)