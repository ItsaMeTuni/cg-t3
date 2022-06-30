from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from textures import *
from vec import Vec

tile_size = 50

class Tile:

    def __init__(self, tile_x, tile_y, color = (1, 1, 1)):
        self.is_destroyed = False
        self.position = Vec(tile_x * tile_size, 0, tile_y * tile_size)
        self.color = color

    def tick(self, delta):
        pass

    def render(self):
        glColor3f(*self.color)

        glPushMatrix()
        glTranslatef(self.position.x, 0, self.position.z)

        glBegin(GL_QUADS)
        glNormal3f(0, 1, 0)

        glTexCoord2f(0, 0)
        glVertex3f(0, 0, 0)

        glTexCoord2f(1, 0)
        glVertex3f(0, 0, tile_size)

        glTexCoord2f(1, 1)
        glVertex3f(tile_size, 0, tile_size)

        glTexCoord2f(0, 1)
        glVertex3f(tile_size, 0, 0)

        glTexCoord2f(0, 0)
        glVertex3f(0, 0, 0)
        glEnd()

        glPopMatrix()