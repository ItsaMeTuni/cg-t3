from OpenGL.GL import *
from vec import Vec

entities = []

class Entity:
    def __init__(self, model, hitbox_radius):
        self.model = model
        self.position = Vec(0, 0)
        self.rotation = 0
        self.hitbox_radius = hitbox_radius
        self.is_destroyed = False

    def tick(self, delta):
        pass

    def render(self):
        glPushMatrix()
        glTranslatef(self.position.x, self.position.y, 0)
        glRotatef(self.rotation, 0, 0, 1)
        self.model.render()
        glPopMatrix()

    def destroy(self):
        self.is_destroyed = True

    def do_collision_test(self, other):
        other_hitbox_radius = other.hitbox_radius

        diff = self.position - other.position
        dist = diff.magnitude()

        collides = dist <= other_hitbox_radius + self.hitbox_radius

        return collides
        

    def hitbox_contains_point(self, point):
        hitbox = self.get_hitbox()
        hitbox_min = hitbox[0]
        hitbox_max = hitbox[1]

        return (point.x >= hitbox_min.x and point.x <= hitbox_max.x and
            point.y >= hitbox_min.y and point.y <= hitbox_max.y)

    def collision_enter(self, other):
        pass
