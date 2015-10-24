from pico2d import *

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

class Ai1:
    def __init__(self):
        self.image = load_image('AI1.png')

    def draw(self):
        self.image.clip_draw(0,0,100,100,400,750)




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

user=User()

ground=Ground()

audience1=Audience1()

audience2=Audience2()

ball=Ball()

ai1=Ai1()
running= True;
x, y = 100, 100

while running:
     handle_events()


     clear_canvas()
     ground.draw()
     user.draw()
     audience1.draw()
     audience2.draw()
     ball.draw()
     ai1.draw()


     update_canvas()
     delay(0.001)

close_canvas()
