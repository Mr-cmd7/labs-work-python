class Object:
    def __init__(self, mass=0, velocity=0):
        self.mass = mass
        self.velocity = velocity

    def get_kinetic_energy(self):
        return 0.5 * self.mass * self.velocity ** 2

    def __repr__(self):
        return f'Object(mass={self.mass}, velocity={self.velocity})'