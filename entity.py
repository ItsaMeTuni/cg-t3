from OpenGL.GL import *
from vec import Vec

entities = []

class Entity:
    def __init__(self, model, hitbox_radius):
        self.model = model
        self.position = Vec(0, 0, 0)
        self.rotation_axis = Vec(0, 1, 0)
        self.rotation_angle = 0
        self.is_destroyed = False

    def tick(self, delta):
        pass

    def render(self):
        if self.model is not None:
            glPushMatrix()
            glTranslatef(self.position.x, self.position.y, 0)
            glRotatef(self.rotation_angle, self.rotation_axis.x, self.rotation_axis.y, self.rotation_axis.z)
            self.model.render()
            glPopMatrix()

    def destroy(self):
        self.is_destroyed = True

    def do_collision_test(self, other):
        return False
        

    def hitbox_contains_point(self, point):
        return False

    def collision_enter(self, other):
        pass
