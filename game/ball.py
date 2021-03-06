import random

from pico2d import *

class Ball:
    PIXEL_PER_METER = (10.0 / 0.3) # 10 PIXEL 30cm
    RUN_SPEED_KMPH = 70.0          # Km / Hour 공속도조절
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS *  PIXEL_PER_METER) #초당 몇 픽셀?

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8
    sound =None
    goal = None


    def __init__(self):
        self.x , self.y = 400, 300
        self.frame = 7
        self.run_frames = 0
        self.distance_x = 0
        self.distance_y = 0
        self.count_user = 0
        self.count_ai = 0
        self.r = 0
        self.image = load_image('resource/etc/SoccerBall.png')
        if Ball.sound == None:
            Ball.sound = load_wav('sound/ball_sound.wav')
            Ball.sound.set_volume(16)
        if Ball.goal == None:
            Ball.goal = load_wav('sound/goal.wav')
            Ball.goal.set_volume(32)



    def update(self, frame_time):
        self.frame = (self.frame + 1) % 1
        self.y += self.distance_y
        self.x += self.distance_x
        self.r = random.randint(0,10)
        if self.x > 325 and self.x <475 and self.y > 770 :
            self.goal.play()
            self.y = 300
            self.x = 400
            self.distance_y = 0
            self.distance_x = 0
            self.count_user = 1

        if  self.x > 325 and self.x <475 and self.y < 100:
            self.goal.play()
            self.y = 300
            self.x = 400
            self.distance_y = 0
            self.distance_x = 0
            self.count_ai = 1



        if self.y > 770 and self.x < 325:
            self.distance_y = Ball.RUN_SPEED_PPS * frame_time*(-1)
            self.sound.play()

        if self.y > 770 and self.x > 475:
            self.distance_y = Ball.RUN_SPEED_PPS * frame_time*(-1)
            self.sound.play()


        if self.y < 100 and self.x < 325:
            self.distance_y = Ball.RUN_SPEED_PPS * frame_time
            self.sound.play()

        if self.y <100 and self.x > 475:
            self.distance_y = Ball.RUN_SPEED_PPS * frame_time
            self.sound.play()

        if self.x > 650:
            self.distance_x = Ball.RUN_SPEED_PPS * frame_time*(-1)
            self.sound.play()


        if self.x < 150:
            self.distance_x = Ball.RUN_SPEED_PPS * frame_time
            self.sound.play()



    def draw(self):
        self.image.clip_draw(0,0,50,48,self.x, self.y)


    def get_bb(self):
        return self.x - 20, self. y - 20, self. x + 20, self.y + 20



    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def moveball_up(self,frame_time):
        self.distance_x = 0
        self.sound.play()
        self.distance_y = Ball.RUN_SPEED_PPS * frame_time


    def moveball_down(self,frame_time):
        self.distance_x = 0
        self.sound.play()
        self.distance_y = Ball.RUN_SPEED_PPS * frame_time*(-1)


    def moveball_right(self,frame_time):
        self.distance_x = 0
        self.distance_y = 0
        self.sound.play()
        self.distance_x = Ball.RUN_SPEED_PPS * frame_time


    def moveball_left(self,frame_time):
        self.distance_x = 0
        self.distance_y = 0
        self.sound.play()
        self.distance_x = Ball.RUN_SPEED_PPS * frame_time*(-1)


    def moveball_up_right(self,frame_time):
        self.distance_x = 0
        self.distance_y = 0
        self.sound.play()
        self.distance_y = Ball.RUN_SPEED_PPS * frame_time
        self.distance_x = Ball.RUN_SPEED_PPS * frame_time*(self.r/4)


    def moveball_up_left(self,frame_time):
        self.distance_x = 0
        self.distance_y = 0
        self.sound.play()
        self.distance_y = Ball.RUN_SPEED_PPS * frame_time
        self.distance_x = Ball.RUN_SPEED_PPS * frame_time*(-1)*(self.r/4)


    def moveball_down_left(self,frame_time):
        self.distance_x = 0
        self.distance_y = 0
        self.sound.play()
        self.distance_y = Ball.RUN_SPEED_PPS * frame_time*(-1)
        self.distance_x = Ball.RUN_SPEED_PPS * frame_time*(-1)*(self.r/4)


    def moveball_down_right(self,frame_time):
        self.distance_x = 0
        self.distance_y = 0
        self.sound.play()
        self.distance_y = Ball.RUN_SPEED_PPS * frame_time*(-1)
        self.distance_x = Ball.RUN_SPEED_PPS * frame_time*(self.r/4)

