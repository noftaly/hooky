import math

class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    @staticmethod
    def from_tuple(tuple_):
        return Vector(tuple_[0], tuple_[1])

    # Operations
    def __sub__(self, other): # self - other
        """ Subtraction by a vector or a scalar. """
        if isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)
        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, other): # self + other
        """ Addition with a vector or a scalar. """
        if isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar): # self * scalar
        """ Multiplication of a vector by a scalar. """
        if isinstance(scalar, (int, float)):
            return Vector(self.x*scalar, self.y*scalar)
        raise TypeError('Can only multiply Vector by a scalar')

    def __truediv__(self, scalar): # self / scalar
        """ Divide of a vector by a scalar. """
        if isinstance(scalar, (int, float)):
            return Vector(self.x / scalar, self.y / scalar)
        raise TypeError('Can only divide Vector by a scalar')

    def __floordiv__(self, scalar): # self // scalar
        """ Floor-divide of a vector by a scalar. """
        if isinstance(scalar, (int, float)):
            return Vector(self.x // scalar, self.y // scalar)
        raise TypeError('Can only true-divide Vector by a scalar')

    def __abs__(self): # abs(self)
        """ Absolute value (magnitude) of the vector. """
        return self.mag()

    def __str__(self): # str(self)
        """ Human-readable string representation of the vector. """
        return f'(x={self.x}, y={self.y})'


    # Useful methods
    def mag(self):
        """ Magnitude of the vector. """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self, val):
        """ Normalize a vector. """
        magnitude = self.mag()
        if magnitude != 0:
            return self * ((1 / magnitude) * val)
        return self

    def with_ints(self):
        self.x = int(self.x)
        self.y = int(self.y)
        return self

    def as_tuple(self):
        return (self.x, self.y)

    def angle_with(self, other):
        return math.acos(((self.x/64) * (other.x/64) + (self.y/64) * (other.y/64)) / (self.mag() + other.mag()))

    def apply_angle(self, angle):
        self.x = self.x * math.cos(angle) - math.sin(angle) * self.y
        self.y = self.x * math.sin(angle) + math.cos(angle) * self.y
