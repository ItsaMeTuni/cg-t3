from random import randint, uniform
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from colors import colors
from textures import *
from vec import Vec
from tile import Tile, tile_size

class BuildingTile(Tile):
    def __init__(self, tile_x, tile_y):
        super().__init__(tile_x, tile_y, (0.3, 0, 0))

        self.height = uniform(50, 150)
        self.color = colors[randint(0, len(colors) - 1)]

    def render(self):
        glColor3f(*self.color)

        glPushMatrix()

        glTranslatef(self.position.x + tile_size/2, self.height / 2, self.position.z + tile_size/2)
        glScale(tile_size, self.height, tile_size)

        glutSolidCube(1)

        glPopMatrix()