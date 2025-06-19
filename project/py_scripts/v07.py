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

def Subsystem_driver():
    print("Testing idle")
    led_pedestrian_red.show_stop()
    led_pedestrian_green.show_stop()
    sleep(1)
    print("Testing green")
    TrafficLightSubsystem.show_amber()
    sleep(1)
    TrafficLightSubsystem.show_red()
    PedestrianSubsystem.show_walk
    sleep(1)