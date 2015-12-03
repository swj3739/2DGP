import game_framework
import round_1
from pico2d import *


name = "TitleState"
image = None

def enter():
    global image
    image = load_image('resource/etc/title.png')





def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.push_state(round_1)
                


def draw():
    clear_canvas()
    image.draw(400,400)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






