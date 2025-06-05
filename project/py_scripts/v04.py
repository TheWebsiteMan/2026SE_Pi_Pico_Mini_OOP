from time import sleep
from led_light import Led_Light




red_light = Led_Light(3, False, False)

while True:
    red_light.flash()
    sleep(3)