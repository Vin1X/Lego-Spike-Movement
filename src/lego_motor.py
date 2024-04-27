from buildhat import Motor


class Lego_Motor:
    def __init__(self, port):
        self.port = port
        self.motor = Motor(port)
        self.state = self.motor.connected

    def start(self):
        self.motor.start()

    def stop(self):
        self.motor.stop()

    def forwards(self, speed=100):
        self.motor.start(speed)

    def backwards(self, speed=-100):
        self.motor.start(speed)

    def speed(self, speed):
        self.motor.set_default_speed(speed)
