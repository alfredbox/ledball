from sense_hat import SenseHat
import math

from check_goal import check_goal
from check_wall import check_wall
from draw import draw_ball, draw_wall, draw_goal

sense = SenseHat()

g = (3,2)
w = [(3,4), (3,3), (2,3)]
reset = True

while True:
    while not reset:
        b = draw_ball(b)
        hit_goal = check_goal(b, g)
        hit_wall = check_wall(b, w)
        if hit_goal or hit_wall:
            reset = True
    sense.clear()
    draw_wall(w)
    draw_goal(g)
    b = (7,7)
    reset = False

