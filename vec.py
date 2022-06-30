from math import cos, sin, radians, sqrt, acos, degrees
import numpy as np

def rotation_matrix(axis, theta):
    """
    https://stackoverflow.com/a/6802723
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = np.asarray(axis)
    axis = axis / sqrt(np.dot(axis, axis))
    a = cos(theta / 2.0)
    b, c, d = -axis * sin(theta / 2.0)
    aa, bb, cc, dd = a * a, b * b, c * c, d * d
    bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
    return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                     [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                     [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])


class Vec:
    def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
    
    def rotate(self, deg, axis):
        v = [self.x, self.y, self.z]
        axis = [axis.x, axis.y, axis.z]
        theta = radians(deg)

        x, y, z = np.dot(rotation_matrix(axis, theta), v)

        return Vec(x, y, z)

    def magnitude(self):
        return sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def angle_between(self, other):
        angle_in_radians = acos(self.dot(other)/(self.magnitude() * other.magnitude()))
        angle = degrees(angle_in_radians)
        
        if (other - self).x > 0:
            return -angle
        else:
            return angle

    def dot(self, other):
        x, y, z = np.dot([self.x, self.y, self.z], [other.x, other.y, other.z])
        return Vec(x, y, z)

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
        z = self.z + other.z
        return Vec(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vec(x, y, z)

    def __mul__(self, other: int):
        x = self.x * other
        y = self.y * other
        z = self.z * other
        return Vec(x, y, z)

    def __truediv__(self, other: int):
        x = self.x / other
        y = self.y / other
        z = self.z / other
        return Vec(x, y, z)

    def __str__(self):
        return f'(x: {self.x} , y: {self.y}, z: {self.z})'

