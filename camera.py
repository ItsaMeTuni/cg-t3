from entity import Entity
from vec import Vec
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import mouse



class Camera:

    def __init__(self, car):
        self.position = Vec(50, 30, 50)
        self.accumulated_mouse_pos = Vec(0, 0, 0)
        self.sensitivity = .1
        self.car = car
        self.is_destroyed = False

    def render(self):
        pass

    def tick(self, delta):
        # self.accumulated_mouse_pos += mouse.position - Vec(250, 250, 0)

        # forward = Vec(0, 0, 1).rotate(-self.accumulated_mouse_pos.x / (1/self.sensitivity), Vec(0, 1, 0)).rotate(self.accumulated_mouse_pos.y / (1/self.sensitivity), Vec(1, 0, 0))
        # target = self.position + forward

        # glutWarpPointer(250, 250)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(self.position.x, self.position.y, self.position.z, self.car.position.x, self.car.position.y, self.car.position.z, 0, 1, 0)

