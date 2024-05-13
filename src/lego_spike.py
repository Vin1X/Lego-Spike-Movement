from lego_color_sensor import LegoColorSensor
from lego_motor import LegoMotor
from buildhat import Hat
from lego_motor_pair import LegoMotorPair


class Lego_Spike:
    def __init__(self):
        self.color_sensor = LegoColorSensor("A")
        self.hat = Hat()
        self.motor_pair = LegoMotorPair("D", "C")
        self.max_speed = 20
        self.max_absolute_difference = 50

    def follow_line(self):
        right_speed, left_speed = self.calculate_steering()
        self.motor_pair.start(speedr=right_speed, speedl=left_speed)

    def calculate_steering(self, diff=None):
        diff = self.color_sensor.reflected_light() - 50
        reduced_speed = (self.max_speed * 2) / self.max_absolute_difference * abs(diff) - self.max_speed
        if diff < 0:
            left_speed = self.max_speed - reduced_speed
            right_speed = - self.max_speed
        else:
            left_speed = self.max_speed
            right_speed = reduced_speed
        return right_speed, left_speed
