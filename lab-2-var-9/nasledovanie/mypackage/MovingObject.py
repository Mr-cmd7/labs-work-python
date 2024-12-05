from .Object import Object

class MovingObject(Object):
    def __init__(self, mass=0, velocity=0, force=0):
        super().__init__(mass, velocity)
        self.force = force

    def calculate_work(self, distance):
        return self.force * distance

    def __repr__(self):
        return f'MovingObject(mass={self.mass}, velocity={self.velocity}, force={self.force})'