from entity import Entity
from vec import Vec
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import mouse



class Camera(Entity):

    def __init__(self):
        super().__init__(None, 0)

        self.position = Vec(0, 50, 0)
        self.accumulated_mouse_pos = Vec(0, 0, 0)
        self.sensitivity = .1

    def tick(self, delta):
        super().tick(delta)

        self.accumulated_mouse_pos += mouse.position - Vec(250, 250, 0)

        forward = Vec(0, -1, 0).rotate(-self.accumulated_mouse_pos.x / (1/self.sensitivity), Vec(0, 1, 0)).rotate(self.accumulated_mouse_pos.y / (1/self.sensitivity), Vec(1, 0, 0))
        target = self.position + forward

        glutWarpPointer(250, 250)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(self.position.x, self.position.y, self.position.z, target.x, target.y, target.z, 0, 1, 0)

