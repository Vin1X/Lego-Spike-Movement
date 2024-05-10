from buildhat import ColorSensor


# Wrapper class for color sensor
class LegoColorSensor:
    # parse ports and activate by default
    def __init__(self, port):
        self.port = port
        self.sensor = ColorSensor(port)
        self.sensor.on()

    # Ambient light
    def ambient_light(self):
        return self.sensor.get_ambient_light()

    # Current color, less useful since not accurate
    def color(self):
        return self.sensor.get_color()

    # Color in hsv format
    def color_hsv(self):
        return self.sensor.get_color_hsv()

    # Color in rgbi format
    def color_rgbi(self):
        return self.sensor.get_color_rgbi()

    # Current reflektion in %
    def reflected_light(self):
        return self.sensor.get_reflected_light()

    # Turn on
    def on(self):
        self.sensor.on()

    # Turn off
    def off(self):
        self.sensor.off()

    # RGB to hsv format
    def rgb_to_hsv(self, red, green, blue):
        return self.sensor.rgb_to_hsv(red, green, blue)

    # Color name based on RGB values
    def segment_color(self, red, green, blue):
        return self.sensor.segment_color(red, green, blue)

    # Wait until specific color
    def wait_until_color(self, color):
        return self.sensor.wait_until_color(color)
