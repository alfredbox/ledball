from sense_hat import SenseHat
sense = SenseHat()

def check_goal(b, g):
    if b==g:
        sense.show_message("GOAL!")
        return True
    return False
