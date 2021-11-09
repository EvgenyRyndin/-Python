class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self):
        mass = self._length * self._width * 25 * 5 / 1000
        return mass


random_road = Road(45, 5544)
print(random_road.calc_mass(), 'т')