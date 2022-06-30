from vec import Vec
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

class Fuel:
    def __init__(self):
        self.position = Vec(600, 10, 540)
        self.is_destroyed = False
    
    def tick(self, delta):
        pass

    def render(self):
        glPushMatrix()
        glTranslatef(self.position.x, self.position.y, self.position.z)
        glColor3f(0, 1, 0)
        glutSolidSphere(5, 25, 25)
        glPopMatrix()

