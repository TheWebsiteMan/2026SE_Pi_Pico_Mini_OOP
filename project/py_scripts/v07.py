from controller import TrafficLightSubsystem, PedestrianSubsystem
from led_light import Led_Light
from button import Pedestrian_Button
from audio_notification import Audio_Notification
from time import sleep

led_pedestrian_red = Led_Light(19, True, True)
led_pedestrian_green = Led_Light(17, False, True)
led_traffic_red = Led_Light(3, False, True)
led_traffic_amber = Led_Light(5, False, True)
led_traffic_green = Led_Light(6, False, True)
pedestrian_button = Pedestrian_Button(22, True)
buzzer = Audio_Notification(27, True)
traffic_driver = TrafficLightSubsystem(led_traffic_red, led_traffic_amber, led_traffic_green, True)
pedestrian_driver = PedestrianSubsystem(led_pedestrian_red, led_pedestrian_green, pedestrian_button, buzzer, True)

def subsystem_driver():
    print("Testing Red")
    sleep(1)
    traffic_driver.show_red()
    print("Pass: Red ON, Amber OFF, Green OFF")
    sleep(5)
    print("Testing Amber")
    sleep(1)
    traffic_driver.show_amber()
    print("Pass: Red OFF, Amber ON, Green OFF")
    sleep(5)
    print("Testing Green")
    sleep(1)
    traffic_driver.show_green()
    print("Pass: Red OFF, Amber OFF, Green ON")
    sleep(5)
    print("Testing Stop")
    sleep(1)
    pedestrian_driver.show_stop()
    print("Pass: Red ON, Green OFF, Buzzer OFF")
    sleep(5)
    print("Testing Walk")
    sleep(1)
    pedestrian_driver.show_walk()
    print("Pass: Red OFF, Green ON, Buzzer ON")
    sleep(5)
    print("Testing Warning")
    sleep(1)
    i = 0
    while(i<5):
        pedestrian_driver.show_warning()
        print("Pass: Red FLASHING, Green OFF, Buzzer ?")
        i = i+1
    sleep(5)

if (input() == "flash"):
    i = 0
    while(i<5):
        pedestrian_driver.show_warning()
        print("Pass: Red FLASHING, Green OFF, Buzzer ?")
        sleep(1)
        i = i+1
else:
    subsystem_driver()