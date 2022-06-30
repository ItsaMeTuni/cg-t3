from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from PIL import Image
import numpy as np

asphalt_texture_id = 0

def get_asphalt_texture_id():
    return asphalt_texture_id

def load_textures():
    print('load')
    global asphalt_texture_id

    asphalt_texture_id = glGenTextures(1)
    load_texture(asphalt_texture_id, 'asphalt.jpg')
    print(asphalt_texture_id)

def load_texture(texture_id, path):
    img = Image.open(path)
    img_data = np.array(list(img.getdata()), np.int8)

    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    # texture wrapping params
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    # texture filtering params
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0,
                 GL_RGB, GL_UNSIGNED_BYTE, img_data)