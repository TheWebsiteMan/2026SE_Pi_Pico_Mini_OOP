from controller import Controller, TrafficLightSubsystem, PedestrianSubsystem
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
subsystem_wrangler = Controller(led_pedestrian_red, led_pedestrian_green, led_traffic_red, led_traffic_amber, led_traffic_green, pedestrian_button, buzzer, True)

def wrangler_test():
    print("Testing IDLE")
    sleep(0.5)
    subsystem_wrangler.set_idle_state()
    print("Pass: Red OFF, Amber OFF, Green ON, P_Red ON, P_Green OFF, Buzzer OFF")
    sleep(2)
    print("Testing CHANGE")
    sleep(0.5)
    subsystem_wrangler.set_change_state()
    print("Pass: Red OFF, Amber ON, Green OFF, P_Red ON, P_Green OFF, Buzzer OFF")
    sleep(2)
    print("Testing WALK")
    sleep(0.5)
    subsystem_wrangler.set_walk_state()
    print("Pass: Red ON, Amber OFF, Green OFF, P_Red OFF, P_Green ON, Buzzer ON")
    sleep(2)
    print("Testing WARNING")
    sleep(0.5)
    subsystem_wrangler.set_warning_state()
    print("Pass: Red ON, Amber OFF, Green OFF, P_Red FLASH, P_Green OFF, Buzzer OFF")
    sleep(2)
    print("Testing ERROR")
    sleep(0.5)
    subsystem_wrangler.error_state()
    print("Pass: Amber FLASHING, All else: OFF")
    sleep(2)