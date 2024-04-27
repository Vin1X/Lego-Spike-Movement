from buildhat import ColorSensor


class Lego_Color_Sensor:
    def __init__(self, port):
        self.port = port
        self.sensor = ColorSensor(port)
        self.state = self.sensor.connected

    def get_color(self):
        return self.sensor.get_color()

    def get_reflected_light_intensity(self):
        return self.sensor.get_reflected_light_intensity()

    def get_ambient_light_intensity(self):
        return self.sensor.get_ambient_light_intensity()
