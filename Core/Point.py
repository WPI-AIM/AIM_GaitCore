import numpy as np

class Point(object):

    def __init__(self,x,y,z):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

    @z.setter
    def z(self, value):
        self._z = value

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z

        return Point(x, y, z)

    def __mul__(self, other):
        x = other * self.x
        y = other * self.y
        z = other * self.z
        return Point(x, y, z)

    def __rmul__(self, other):
       return self.__mul__(other)

    def __str__(self):
        return " X: " + str(self.x) + " Y: " + str(self.y) + " Z: " + str(self.z)

    def toarray(self):
        return np.array((self.x, self.y, self.z))
