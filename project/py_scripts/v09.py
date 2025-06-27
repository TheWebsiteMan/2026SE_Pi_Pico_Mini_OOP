from time import sleep
from controller import Controller, TrafficLightSubsystem, PedestrianSubsystem
from led_light import Led_Light
from button import Pedestrian_Button
from audio_notification import Audio_Notification


led_pedestrian_red = Led_Light(19, True, True)
led_pedestrian_green = Led_Light(17, False, True)

led_traffic_red = Led_Light(3, False, True)
led_traffic_amber = Led_Light(5, False, True)
led_traffic_green = Led_Light(6, False, True)

pedestrian_button = Pedestrian_Button(22, True)

buzzer = Audio_Notification(27, True)

traffic_driver = TrafficLightSubsystem(led_traffic_red, led_traffic_amber, led_traffic_green, True)

pedestrian_driver = PedestrianSubsystem(led_pedestrian_red, led_pedestrian_green, pedestrian_button, buzzer, True)

subsystem_wrangler = Controller(led_pedestrian_red, led_pedestrian_green, led_traffic_red, led_traffic_amber, led_traffic_green, pedestrian_button, buzzer, True)

while True:
    subsystem_wrangler.update()
    sleep(0.1)