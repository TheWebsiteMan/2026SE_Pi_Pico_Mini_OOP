class Audio_Notification:
    def __init__(self, pin, debug):
        self.__pin = pin
        self.__debug = False
    def warning_on(self):
        print("Beep")
    def warning_off(self):
        pass