import math

class Vector:
    def __init__(self, x, y):
        self.x , self.y = x, y

    @staticmethod
    def from_tuple(tuple):
        return Vector(tuple[0], tuple[1])

    # Operations
    def __sub__(self,other):
        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        """ Vector addition. """
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        """ Multiplication of a vector by a scalar. """
        if isinstance(scalar, int) or isinstance(scalar, float):
            return Vector(self.x*scalar, self.y*scalar)
        raise NotImplementedError('Can only multiply Vector by a scalar')

    def __truediv__(self, scalar):
        """ Divide of a vector by a scalar. """
        if isinstance(scalar, int) or isinstance(scalar, float):
            return Vector(self.x / scalar, self.y / scalar)
        raise NotImplementedError('Can only divide Vector by a scalar')

    def __floordiv__(self, scalar):
        """ Floor-divide of a vector by a scalar. """
        if isinstance(scalar, int) or isinstance(scalar, float):
            return Vector(self.x // scalar, self.y // scalar)
        raise NotImplementedError('Can only divide Vector by a scalar')

    def __abs__(self):
        """ Absolute value (magnitude) of the vector. """
        return math.sqrt(self.x**2 + self.y**2)
    
    def __str__(self):
        """ Human-readable string representation of the vector. """
        return f'(x={self.x}, y={self.y})'

    
    # Useful methods
    def mag(self):
        """ Magnitude of the vector. """
        return math.sqrt(self.x**2 + self.y**2)
   
    def normalize(self,val):
        """ Normalize a vector. """
        magnitude = self.mag()
        if magnitude != 0:
            return self * ((1/magnitude) * val)
        return self
    
    def with_ints(self):
        self.x = int(self.x)
        self.y = int(self.y)

    def as_tuple(self):
        return (self.x, self.y)

    def cast(self, pos):
        return Vector(pos.x + self.x, pos.y + self.y)
