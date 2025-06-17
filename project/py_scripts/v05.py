from button import Pedestrian_Button
from time import sleep
from random import randint
button = Pedestrian_Button(22, False)


while True:
    timer = 0
    if button.button_state == False:
        sleep(randint(1, 10))
        print("Press NOW!!!")
        sleep(2)
        if button.button_state == True:
            print(f"Congratulations!")
        else:
            print("You are SLOW")
