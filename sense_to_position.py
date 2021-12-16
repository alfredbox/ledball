from sense_hat import SenseHat
import math
sense = SenseHat()

def sense_to_position():
    axel = sense.get_accelerometer_raw()
    x = sensitivity(axel['x'])
    y = sensitivity(axel['y'])
    return (x,y)


def sensitivity(accel_n):
    pos = math.ceil(accel_n * 6)+ 4
    pos = 7 if pos > 7 else pos
    pos = 0 if pos < 0 else pos
    return int(pos)




