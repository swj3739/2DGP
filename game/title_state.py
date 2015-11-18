import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None
press=None


def enter():
    global image,press
    image = load_image('resource/etc/title.png')
    press = load_image('resource/etc/press.png')


def exit():
    global image,press
    del(image)
    del(press)
    close_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.push_state(main_state)


def draw():
    clear_canvas()
    image.draw(400,300)
    press.draw(400,120)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






