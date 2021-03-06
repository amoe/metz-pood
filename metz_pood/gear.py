class Gear:
    def __init__(self, chainring, cog, wheel, observer):
        self.chainring = chainring
        self.cog = cog
        self.wheel = wheel
        self.observer = observer

    def gear_inches(self):
        return self.ratio() * self.wheel.width()

    def ratio(self):
        return self.chainring / float(self.cog)

    def set_cog(self, new_cog):
        self.cog = new_cog
        self.changed()

    def set_chainring(self, new_chainring):
        self.chainring = new_chainring
        self.changed()

    def changed(self):
        # This method is a 'command' in the Metz sense.  It can potentially
        # have side effects, its value is not used.  As such we must test
        # that it gets sent, using a mock.
        self.observer.changed(self.chainring, self.cog)
