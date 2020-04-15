class Bicycle:
    def __init__(self, **opts):
        self.size = opts.get('size')
        self.chain = opts.get('chain')
        if self.chain is None:
            self.chain = self.default_chain()
        self.tire_size = opts.get('tire_size')
        if self.tire_size is None:
            self.tire_size = self.default_tire_size()
        self.post_initialize(opts)

    def spares(self):
        result = {'tire_size': self.tire_size,
                'chain': self.chain}
        result.update(self.local_spares())
        return result

    def default_tire_size(self):
        raise NotImplementedError()
    
    def post_initialize(self, opts):
        pass

    def local_spares(self):
        return {}

    def default_chain(self):
        return "11-speed"


class RoadBike(Bicycle):
    def post_initialize(self, opts):
        self.tape_color = opts.get('tape_color')
        

    def local_spares(self):
        return {
            'tape_color': self.tape_color
        }

    def default_tire_size(self):
        return "23"
