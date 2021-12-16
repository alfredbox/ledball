from sense_to_position import sense_to_position
from sense_hat import SenseHat
sense = SenseHat()

BLUE = (0,0,255)
GREEN  = (0,255,0)
RED  = (255,0,0)
CLEAR = (0,0,0)

def draw(pos, color):
    sense.set_pixel(pos[0],pos[1], color)

def draw_goal(g):
    draw(g, GREEN)

def draw_wall(w):
    for brick in w:
        draw(brick,RED)
    

def draw_ball(b):
    new_b = sense_to_position()
    if new_b != b:
        draw(b, CLEAR)
        draw(new_b,BLUE)
    return new_b

