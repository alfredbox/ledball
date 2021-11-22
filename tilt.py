from sense_hat import SenseHat
import math

sense = SenseHat()

while True:
    axel = sense.get_accelerometer_raw()
    pos = math.ceil(axel['x'] * 4) + 4
    sense.clear()
    sense.set_pixel(pos,2, (0,0,255))
