from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from textures import *
from vec import Vec
from tile import Tile

class RoadTile(Tile):
    def render(self):
        glBindTexture(GL_TEXTURE_2D, get_asphalt_texture_id())
        super().render()