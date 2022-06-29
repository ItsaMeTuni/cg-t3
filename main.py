from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import time
import keyboard
from entity import entities

def init():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)

    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)

    window = glutCreateWindow("Matrix Stack")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard.on_down)
    glutKeyboardUpFunc(keyboard.on_up)

    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)
    glClearColor(0, 0, 0, 1)
    glutMainLoop()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10, 10, -10, 10, -1.0, 1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def display():
    global last_display_timestamp
    global entities

    delta = time.time() - last_display_timestamp
    last_display_timestamp = time.time()

    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    for entity in entities:
        entity.tick(delta)
        entity.render()

    do_collision_tests()
    remove_destroyed_entities()
    
    glutSwapBuffers()
    glutPostRedisplay()

def do_collision_tests():
    collisions = []

    for entity in entities:
        if entity.is_destroyed:
            continue

        for other in entities:
            if other is entity or entity.is_destroyed:
                continue

            if (other, entity) in collisions:
                continue
            
            collides = entity.do_collision_test(other)
            if collides:
                entity.collision_enter(other)
                other.collision_enter(entity)

            collisions.append((entity, other))

def remove_destroyed_entities():
    for entity in entities:
        if entity.is_destroyed:
            entities.remove(entity)

init()
