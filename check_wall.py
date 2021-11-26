from sense_hat import SenseHat
sense = SenseHat()

def check_wall(b,w):
    for brick in w:
        if b==brick:
            sense.show_message("game over!")
            return True

    return False


