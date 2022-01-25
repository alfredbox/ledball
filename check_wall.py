from sense_hat import SenseHat
from draw import RED
sense = SenseHat()

def check_wall(b,w):
    for brick in w:
        if b==brick:
            sense.show_message("game over!", text_colour=RED)
            return True

    return False


