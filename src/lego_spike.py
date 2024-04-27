from lego_color_sensor import Lego_Color_Sensor as ColorSensor
from lego_motor import Lego_Motor as Motor
from buildhat import Hat


class Lego_Spike:
    def __init__(self):
        self.motora = Motor("A")
        self.motorb = Motor("B")
        self.color_sensor = ColorSensor("C")
        self.hat = Hat()

    def start_up(self):
        print(self.hat.get())

    def straight(self):
        self.motora.forwards()
        self.motorb.forwards(-100)  # 2nd motor is reversed
