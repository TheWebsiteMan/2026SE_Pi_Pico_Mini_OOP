from pedestrian_button import Pedestrian_Button
from time import sleep

button = Pedestrian_Button(22, True)

while True:
    button.callback()
    print("Waiting for button")
    sleep(0.1)