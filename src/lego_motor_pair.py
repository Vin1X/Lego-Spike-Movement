from buildhat import MotorPair


# Wrapper class for motor pair
class LegoMotorPair:
    # Parse ports
    def __init__(self, port_1, port_2):
        self.motor_pair = MotorPair(port_1, port_2)

    # Run for specific amount of degrees
    def run_degrees(self, degrees, speedl=None, speedr=None):
        self.motor_pair.run_for_degrees(degrees, speedl, speedr)

    # Run for specific amount of rotations
    def run_rotations(self, rotations, speedl=None, speedr=None):
        self.motor_pair.run_for_rotations(rotations, speedl, speedr)

    # Run for specific amount of seconds
    def run_seconds(self, seconds, speedl=None, speedr=None):
        self.motor_pair.run_for_seconds(seconds, speedl, speedr)

    # Run to certain position in degrees
    def run_position(self, degreesl, degreesr, speed=None, direction="shortest"):
        self.motor_pair.run_to_position(degreesl, degreesr, speed, direction)

    # Set default run speed
    def default_speed(self, speed):
        self.motor_pair.set_default_speed(speed)

    # Choose if rpm as unit for speed
    def speed_unit(self, rpm=False):
        self.motor_pair.set_speed_unit_rpm(rpm)

    # Start motor with specific speed for each motor
    def start(self, speedl=None, speedr=None):
        self.motor_pair.start(speedl, speedr)

    # Stop motor
    def stop(self):
        self.motor_pair.stop()
