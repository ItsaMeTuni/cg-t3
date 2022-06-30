from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import time
import keyboard
from entity import entities
import mouse
from vec import Vec
from camera import Camera
from car import Car
from textures import *
from road_tile import RoadTile

def init():
    global asphalt_texture_id

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)

    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)

    entities.append(Camera())
    entities.append(Car())
    entities.append(RoadTile())

    window = glutCreateWindow("T3")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard.on_down)
    glutKeyboardUpFunc(keyboard.on_up)
    glutPassiveMotionFunc(mouse.on_move)

    glClearDepth(1.0) 
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)
    glEnable(GL_TEXTURE_2D)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    load_textures()

    glClearColor(0, 0, 0, 1)
    glutMainLoop()

def reshape(w, h):
    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, w/h, 0.01, 5000)

last_display_timestamp = time.time()
def display():
    global last_display_timestamp
    global entities

    delta = time.time() - last_display_timestamp
    last_display_timestamp = time.time()

    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glMatrixMode(GL_MODELVIEW)
    # glLoadIdentity()




    # glMatrixMode(GL_MODELVIEW)
    # glLoadIdentity()
    # gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)

    for entity in entities:
        entity.tick(delta)
        entity.render()

    # do_collision_tests()
    remove_destroyed_entities()
    
    glutSwapBuffers()
    glutPostRedisplay()

# last_mouse_pos = Vec(0, 0)
# last_camera_target = Vec(0, 0)
# def update_camera():
#     global last_mouse_pos, last_camera_target

#     delta_pos = mouse.position - last_mouse_pos


#     gluLookAt(*last_camera_target, 0, 0, 0, 0, 1, 0)

#     last_mouse_pos = mouse.position

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
