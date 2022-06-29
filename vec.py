from math import cos, sin, radians, sqrt, acos, degrees

class Vec:
    def __init__(self, x, y):
            self.x = x
            self.y = y
    
    def rotate(self, deg):
        rad = radians(deg)
        x = self.x * cos(rad) - self.y * sin(rad)
        y = self.x * sin(rad) + self.y * cos(rad)
        return Vec(x, y)

    def magnitude(self):
        return sqrt(self.x*self.x + self.y*self.y)

    def angle_between(self, other):
        angle_in_radians = acos(self.dot(other)/(self.magnitude() * other.magnitude()))
        angle = degrees(angle_in_radians)
        
        if (other - self).x > 0:
            return -angle
        else:
            return angle

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def normalized(self):
        magnitude = self.magnitude()
        if magnitude == 0:
            return self

        return self / self.magnitude()

    def project_onto(self, other):
        other_magnitude = other.magnitude()
        if other_magnitude == 0:
            return other

        return other * (self.dot(other)/(other_magnitude**2))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vec(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vec(x, y)

    def __mul__(self, other: int):
        x = self.x * other
        y = self.y * other
        return Vec(x, y)

    def __truediv__(self, other: int):
        x = self.x / other
        y = self.y / other
        return Vec(x, y)

    def __str__(self):
        return f'(x: {self.x} , y: {self.y})'

