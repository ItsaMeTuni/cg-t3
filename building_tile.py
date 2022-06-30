from random import uniform
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from textures import *
from vec import Vec
from tile import Tile, tile_size

class BuildingTile(Tile):
    def __init__(self, tile_x, tile_y):
        super().__init__(tile_x, tile_y, (0.3, 0, 0))

        self.height = uniform(50, 150)

    def render(self):
        glPushMatrix()

        glTranslatef(self.position.x, self.height / 2, self.position.z)
        glScale(tile_size, self.height, tile_size)

        glutSolidCube(1)

        glPopMatrix()