from sense_hat import SenseHat
import math

from check_goal import check_goal
from check_wall import check_wall
from draw import draw_ball, draw_wall, draw_goal, draw_trophy
from levels import levels

sense = SenseHat()

lvl_num=0

while True:
    sense.clear()
    level=levels[lvl_num]
    b = level["ball"]
    g = level["goal"]
    w = level["wall"]
    draw_wall(w)
    draw_goal(g)
    playing=True
    while playing:
        b = draw_ball(b)
        hit_goal = check_goal(b, g)
        hit_wall = check_wall(b, w)
        if hit_goal:
            lvl_num = lvl_num + 1
            if lvl_num == len(levels):
                draw_trophy()
                lvl_num = 0
            playing=False
        if hit_wall:
            lvl_num = 0
            playing=False
