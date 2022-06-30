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
        self.fuel = 100
        self.fuel_consumption = 5
        self.is_stopped = False
        self.was_space_pressed_last_frame = False
        self.fuel_items = []
        self.size = 5
        self.min_bounds = Vec(0, 0, 0)
        self.max_bounds = Vec(1000, 0, 1000)


    def tick(self, delta):
        space_pressed = is_key_pressed(b' ')
        if space_pressed and space_pressed != self.was_space_pressed_last_frame:
            self.is_stopped = not self.is_stopped

        self.was_space_pressed_last_frame = space_pressed

        if is_key_pressed(b'a'):
            self.rotation += 90 * delta
        elif is_key_pressed(b'd'):
            self.rotation -= 90 * delta

        if self.fuel <= 0 or self.is_stopped:
            return

        self.position = self.position + Vec(0, 0, self.speed).rotate(self.rotation, Vec(0, 1, 0)) * delta

        self.fuel -= self.fuel_consumption * delta

        for fuel in self.fuel_items:
            if fuel.is_destroyed:
                continue

            if (self.position - fuel.position).magnitude() <= 2.5:
                fuel.is_destroyed = True
                self.fuel += 100

        self.check_bounds_collision()
        
    def render(self):
        glPushMatrix()
        glTranslatef(self.position.x, self.position.y, self.position.z)
        glRotatef(self.rotation, 0, 1, 0)
        glColor3f(0, 0, 1)
        glutSolidCube(5)
        glPopMatrix()

    def check_bounds_collision(self):      
        if self.position.x + self.size >= self.max_bounds.x:
            self.position.x = self.max_bounds.x - self.size 
            
        elif self.position.x - self.size <= self.min_bounds.x:
            self.position.x = self.min_bounds.x + self.size 

        if self.position.z + self.size >= self.max_bounds.z:
            self.position.z = self.max_bounds.z - self.size 

        elif self.position.z - self.size <= self.min_bounds.z:
            self.position.z = self.min_bounds.z + self.size 