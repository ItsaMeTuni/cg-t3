from entity import Entity
from vec import Vec
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import mouse
from keyboard import is_key_pressed

class Camera:

    def __init__(self, car):
        self.position = Vec(500, 50, 500)
        self.accumulated_mouse_pos = Vec(0, 0, 0)
        self.sensitivity = .1
        self.car = car
        self.is_destroyed = False
        self.w = 100
        self.h = 100
        self.min_fov = 20
        self.min_fov_dist = 600

        self.max_fov = 60
        self.max_fov_dist = 5

        self.first_person = True

    def render(self):
        pass

    def tick(self, delta):
        if is_key_pressed(b'1'):
            self.first_person = True
        elif is_key_pressed(b'3'):
            self.first_person = False

        dist_to_car = (self.car.position - self.position).magnitude()
        fov_dist_normalized = (dist_to_car - self.max_fov_dist) / self.min_fov_dist
        fov_dist_normalized_clamped = min(1, max(0, fov_dist_normalized))
        fov = (1 - fov_dist_normalized_clamped) * self.max_fov + fov_dist_normalized_clamped * self.min_fov

        if self.first_person:
            fov = 90

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(fov, self.w/self.h, 0.01, 50000)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        if self.first_person:
            target = self.car.position + Vec(0, 0, 10).rotate(self.car.rotation, Vec(0, 1, 0))
            gluLookAt(self.car.position.x, self.car.position.y, self.car.position.z, target.x, target.y, target.z, 0, 1, 0)
        else:
            gluLookAt(self.position.x, self.position.y, self.position.z, self.car.position.x, self.car.position.y, self.car.position.z, 0, 1, 0)

