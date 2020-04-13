class Wheel:
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire

    def width(self):
        return self.rim + (self.tire * 2)
