class Gear:
    def __init__(self, chainring, cog, wheel, observer):
        self.chainring = chainring
        self.cog = cog
        self.wheel = wheel
        self.observer = observer

    def gear_inches(self):
        return self.ratio() * self.wheel.diameter()

    def ratio(self):
        return self.chainring / float(self.cog)

    def set_cog(self, new_cog):
        self.cog = new_cog
        self.changed()

    def set_chainring(self, new_chainring):
        self.chainring = new_chainring
        self.changed()

    def changed(self):
        observer.changed(self.chainring, self.cog)
