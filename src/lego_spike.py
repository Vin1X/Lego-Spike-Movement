from lego_color_sensor import LegoColorSensor
from lego_motor import LegoMotor
from buildhat import Hat
from lego_motor_pair import LegoMotorPair


class Lego_Spike:
    def __init__(self):
        self.color_sensor_r = LegoColorSensor("C")
        self.color_sensor_l = LegoColorSensor("D")
        self.hat = Hat()
        self.motor_pair = LegoMotorPair("B", "A")
        self.max_speed = 20
        self.max_absolute_difference = 100

    def follow_line(self):
        # diff = self.get_diff_single(self.color_sensor_r)
        diff = self.get_diff_double()
        print(diff)
        right_speed, left_speed = self.calculate_steering(diff)
        self.motor_pair.start(speedr=right_speed, speedl=left_speed)

    def calculate_steering(self, diff: float) -> tuple:
        reduced_speed = (self.max_speed * 2) / self.max_absolute_difference * abs(diff) - self.max_speed
        reduced_speed *= -1
        if diff < 0:
            left_speed = self.max_speed - reduced_speed
            right_speed = - self.max_speed
        else:
            left_speed = self.max_speed
            right_speed = reduced_speed
        return right_speed, left_speed

    def get_diff_single(self, color_sensor) -> float:
        diff = color_sensor.reflected_light() - 50
        return diff

    def get_diff_double(self) -> float:
        l_refl = self.color_sensor_l.reflected_light()
        r_refl = self.color_sensor_r.reflected_light()
        return r_refl - l_refl
