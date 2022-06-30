from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from textures import *

class RoadTile:

    def __init__(self):
        self.is_destroyed = False

    def tick(self, delta):
        pass

    def render(self):
        glBindTexture(GL_TEXTURE_2D, get_asphalt_texture_id())

        glColor3f(0.3, 0.3, 0.3)

        glBegin(GL_QUADS)
        glNormal3f(0, 1, 0)

        glTexCoord2f(0, 0)
        glVertex3f(-10, -2, -10)

        glTexCoord2f(1, 0)
        glVertex3f(-10, -2, 10)

        glTexCoord2f(1, 1)
        glVertex3f(10, -2, 10)

        glTexCoord2f(0, 1)
        glVertex3f(10, -2, -10)

        glTexCoord2f(0, 0)
        glVertex3f(-10, -2, -10)
        glEnd()