from pico2d import *

open_canvas(800,900)

ground=load_image('playground.png')
audience1=load_image('audience1.png')
audience2=load_image('audience2.png')
ground.draw_now(400,510)
audience1.draw_now(50,510)
audience2.draw_now(750,510)
delay(5)
close_canvas()