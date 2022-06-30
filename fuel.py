from vec import Vec
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from tile import tile_size

class Fuel:
    def __init__(self, tile_x, tile_y):
        self.position = Vec(tile_size * tile_x + tile_size/2, 2, tile_size * tile_y + tile_size/2)
        self.is_destroyed = False
    
    def tick(self, delta):
        pass

    def render(self):
        glPushMatrix()
        glTranslatef(self.position.x, self.position.y, self.position.z)
        glColor3f(0, 1, 0)
        glutSolidSphere(2, 25, 25)
        glPopMatrix()

