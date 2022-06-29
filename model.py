from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from random import uniform

pixel_size = 0.5

class Model:

    def __init__(self, width, height, colors, pixels, scale):
        self.colors = colors
        self.width = width
        self.height = height
        self.pixels = pixels
        self.scale = scale * pixel_size


    def render(self):

        glPushMatrix()
        glScalef(self.scale, self.scale, self.scale)

        glBegin(GL_QUADS)
        for x in range(self.width):
            for y in range(self.height):

                pixel_color = self.pixels[y * self.width + x]
                glColor4f(*self.colors[pixel_color])
                
                glVertex3f(-self.width/2 + x, -self.height/2 + (self.height - y), 0)
                glVertex3f(-self.width/2 + x + 1, -self.height/2 + (self.height - y), 0)
                glVertex3f(-self.width/2 + x + 1, -self.height/2 + (self.height - y - 1), 0)
                glVertex3f(-self.width/2 + x, -self.height/2 + (self.height - y - 1), 0)

        glEnd()

        glPopMatrix()


def parse_model(file_path, scale):
    file = open(file_path)

    # skip first line
    file.readline()

    colors = []
    color_count = int(file.readline())
    for _ in range(color_count):
        channels = [float(color) / 255 for color in file.readline().split(' ')]

        alpha = 1
        if len(channels) == 5:
            alpha = channels[4]

        colors.append((channels[1], channels[2], channels[3], alpha))

    # skip blank line
    file.readline()

    # skip section name
    file.readline()
   
    pixels = []
    [row_count, col_count] = [int(value) for value in file.readline().split(' ')]
    for _ in range(row_count):
        row_pixels = [int(pixel) - 1 for pixel in file.readline().split(' ')]
        pixels.extend(row_pixels)

    return Model(col_count, row_count, colors, pixels, scale)



player_model = parse_model('model_player.txt', 0.3)
enemy_model_1 = parse_model('model_enemy_1.txt', 0.3)
enemy_model_2 = parse_model('model_enemy_2.txt', 0.3)
enemy_model_3 = parse_model('model_enemy_3.txt', 0.3)
bullet_model = Model(1, 1, [(0, 0.7, 0.7, 1)], [0], 0.3)
