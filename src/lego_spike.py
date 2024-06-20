from lego_color_sensor import LegoColorSensor
from lego_motor import LegoMotor
from buildhat import Hat
from lego_motor_pair import LegoMotorPair
from simple_pid import PID
import time


class Lego_Spike:
    def __init__(self):
        self.color_sensor_r = LegoColorSensor("C")
        self.color_sensor_l = LegoColorSensor("D")
        self.hat = Hat()

        # Left motor is inverted
        self.motor_pair = LegoMotorPair("A", "B") # A = Left, B = Right
        self.max_speed = 30
        self.max_absolute_difference = 100
        self.pid = PID(.5, .1, 0, setpoint=0)

    def follow_line(self):
        diff = self.get_diff_double()
        diff = self.compute_pid(diff)
        left_speed, right_speed = self.calculate_steering(diff)
        left_speed *= -1
        #:time.sleep(.5)
        self.motor_pair.start(speedl=left_speed, speedr=right_speed)

    def calculate_steering(self, diff: float) -> tuple:
        #print(diff)
        diff = min(100, diff)
        diff = max(-100, diff)
        #print("\t\t", diff, "\n")
        reduced_speed = (self.max_speed * 2) / self.max_absolute_difference * 2 * abs(diff)

        if diff > 0:
            left_speed = self.max_speed - reduced_speed
            right_speed = self.max_speed
        else:
            left_speed = self.max_speed
            right_speed = self.max_speed - reduced_speed
        #print("Reducedspeed:", reduced_speed, "Left:", left_speed, "Right:", right_speed)
        return left_speed, right_speed

    def get_diff_single(self, color_sensor) -> float:
        diff = color_sensor.reflected_light() - 50
        return diff

    # Positive value = deviation to right
    # Negative valu = deviation to left
    def get_diff_double(self) -> float:
        l_refl = self.color_sensor_l.reflected_light()
        r_refl = self.color_sensor_r.reflected_light()
        return r_refl - l_refl

    def compute_pid(self, diff: float) -> float:
        pid_diff = -self.pid(diff)
        print("diff:", diff, "pid:", pid_diff)
        return pid_diff
