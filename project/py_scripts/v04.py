from time import sleep
from led_light import Led_Light




red_light = Led_Light(3, True, False)

red_light.on()
red_light.flash()
