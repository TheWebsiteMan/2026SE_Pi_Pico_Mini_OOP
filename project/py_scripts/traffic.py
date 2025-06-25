from led_light import Led_Light
from time import sleep, time

red_light = Led_Light(3, True, False)


print("Testing on()")
red_light.on()
sleep(0.2)
if red_light.value() == 1:
    print("Passed")
else:
    raise(ValueError)
sleep(0.2)

print("Testing off()")
red_light.off()
sleep(0.2)
if red_light.value() == 0:
    print("Passed")
else:
    raise(ValueError)
sleep(0.2)

print("Testing toggle()")
red_light.toggle()
sleep(0.2)
if red_light.value() == 1:
    print("Passed")
else:
    raise(ValueError)
red_light.toggle()
sleep(0.2)
if red_light.value() == 0:
    print("Passed")
else:
    raise(ValueError)
sleep(0.2)

print("Testing flash()")
red_light.flash()