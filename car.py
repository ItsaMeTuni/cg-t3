from vec import Vec
from keyboard import is_key_pressed, pressed_keys
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

class Car:

    def __init__(self):
        self.position = Vec(10, 2.5, 0)
        self.is_destroyed = False
        self.speed = 100
        self.rotation = 0

    def tick(self, delta):
        self.position = self.position + Vec(0, 0, self.speed).rotate(self.rotation, Vec(0, 1, 0)) * delta
        
        if is_key_pressed(b'a'):
            self.rotation += 90 * delta
        elif is_key_pressed(b'd'):
            self.rotation -= 90 * delta
        
    
    def render(self):
        glPushMatrix()
        glTranslatef(self.position.x, self.position.y, self.position.z)
        glRotatef(self.rotation, 0, 1, 0)
        glColor3f(1, 1, 1)
        glutSolidCube(5)
        glPopMatrix()

        