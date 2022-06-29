from entity import entities
from OpenGL.GL import *

class DebugEntity:
    def __init__(self, base, vector, color, duration):
        self.is_destroyed = False
        self.hitbox_radius = 0

        self.position = base
        self.end = base + vector
        self.remaining_time = duration
        self.color = color

    def render(self):
        glColor(*self.color)

        glBegin(GL_LINES)
        
        glVertex3f(self.position.x, self.position.y, 0.1)
        glVertex3f(self.end.x, self.end.y, 0.1)

        glEnd()

    def tick(self, delta):
        self.remaining_time -= delta
        if self.remaining_time <= 0:
            self.is_destroyed = True

    def do_collision_test(self, other):
        return False

    def collision_enter(self, other):
        pass


def debug_vector(base, vector, color, duration):
    entities.append(DebugEntity(base, vector, color, duration))
