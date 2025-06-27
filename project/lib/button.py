from time import ticks_ms, ticks_diff
from machine import Pin


class Pedestrian_Button(Pin):
    def __init__(self, pin, debug = False):
        super().__init__(pin, Pin.IN, Pin.PULL_DOWN)
        self.__debug = debug
        self.__pin = pin
        self.__last_pressed = 0
        self.__pedestrian_waiting = False
        # set up interrupt on rising edge
        self.irq(trigger=Pin.IRQ_RISING, handler=self.callback)
    
    def button_state(self, value=None):
        if value is None:
            if self.__debug:
                print(f"Button state on Pin {self.__pin} is {'WAITING' if self.__pedestrian_waiting else 'NOT WAITING'}")
            return self.__pedestrian_waiting
        else:
            self.__pedestrian_waiting = bool(value)
            if self.__debug:
                print(f"Button state on Pin {self.__pin} set to {self.__pedestrian_waiting}")
    
    def callback(self, pin):
        current_time = ticks_ms()
        # 200ms delay
        if (ticks_diff(current_time, self.__last_pressed) > 200):
            self.__last_pressed = current_time
            self.__pedestrian_waiting = True
            if self.__debug:
                print(f"Button pressed on Pin {self.__pin} at {current_time}ms")