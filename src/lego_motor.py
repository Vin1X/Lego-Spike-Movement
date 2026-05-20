from buildhat import Motor


# Wrapper class for motor
class LegoMotor:
    # Parse port
    def __init__(self, port):
        self.motor = Motor(port)

    # Run for specific amount of degrees
    def run_degrees(self, degrees, speed=None, blocking=True):
        self.motor.run_for_degrees(degrees, speed, blocking)

    # Run for specific amount of rotations
    def run_rotations(self, rotations, speed=None, blocking=True):
        self.motor.run_for_rotations(rotations, speed, blocking)

    # Run for specific amount of seconds
    def run_seconds(self, seconds, speed=None, blocking=True):
        self.motor.run_for_seconds(seconds, speed, blocking)

    # Run to certain position in degrees
    def run_position(self, degrees, speed=None, blocking=True, direction="shortest"):
        self.motor.run_to_position(degrees, speed, blocking, direction)

    # Set default run speed
    def default_speed(self, speed):
        self.motor.set_default_speed(speed)

    # Choose if rpm as unit for speed
    def speed_unit(self, rpm=False):
        self.motor.set_speed_unit_rpm(rpm)

    # Start motor with specific speed for each motor
    def start(self, speed=None):
        self.motor.start(speed)

    # Stop motor
    def stop(self):
        self.motor.stop()
