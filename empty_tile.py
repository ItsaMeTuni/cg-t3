from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from textures import *
from vec import Vec
from tile import Tile

class EmptyTile(Tile):
    def __init__(self, tile_x, tile_y):
        super().__init__(tile_x, tile_y, (1, 0, 0))

    def render(self):
        glColor3f(0.3, 0, 0)
        super().render()