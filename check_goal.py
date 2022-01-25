from sense_hat import SenseHat
from draw import GREEN
sense = SenseHat()

def check_goal(b, g):
    if b==g:
        sense.show_message("GOAL!", text_colour=GREEN)
        return True
    return False
