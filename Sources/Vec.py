import math

class Vector:
    def __init__(self, x, y):
        self.x , self.y = x, y

#operations
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
    
    def __abs__(self):
        """ Absolute value (magnitude) of the vector. """
        return math.sqrt(self.x**2 + self.y**2)
    

    def __str__(self):
        """ Human-readable string representation of the vector. """
        return f'(x={self.x}, y={self.y})'

    
#useful methods
    def mag(self):
        """ Magnitude of the vector. """
        return math.sqrt(self.x**2 + self.y**2)
   
    def normalize(self,val):
        """ Normalize a vector. """
        magni = self.mag()
        if mag != 0:
            return  self * ((1/mag)*val)
        return self

    def cast(self,pos):
        return pos[0]+self.x,pos[1]+self.y