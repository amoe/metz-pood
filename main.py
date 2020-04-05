class Wheel:
    def __init__(self, rim, tire):
        self.rim = rim
        self.tire = tire

    def diameter(self):
        return rim * (tire * 2)

class Gear:
    def __init__(self, chainring, cog, rim, tire):
        self.chainring = chainring
        self.cog = cog
        self.rim = rim
        self.tire = tire

    def gear_inches(self):
        return self.ratio() * Wheel(rim, tire).diameter()

    def ratio(self):
        return self.chainring / self.cog.to_f()
