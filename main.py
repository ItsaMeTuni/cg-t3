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
from empty_tile import EmptyTile

def init():
    global asphalt_texture_id

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)

    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)


    car = Car()
    entities.append(car)

    entities.append(Camera(car))
    create_map_tiles()


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
    glEnable(GL_LIGHTING)
    glDepthFunc(GL_LESS)
    glDepthMask(GL_TRUE)
    glEnable(GL_COLOR_MATERIAL)
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.4, 0.4, 0.4))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.7, 0.7, 0.7))
    glLightfv(GL_LIGHT0, GL_POSITION, (0, 3, 5))
    glEnable(GL_LIGHT0);
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    load_textures()

    glClearColor(0, 0, 0, 1)
    glutMainLoop()

def create_map_tiles():
    f = open('map.csv')
    lines = f.readlines()

    x = 0
    y = 0
    for line in lines:
        x = 0
        for tile in line.split(','):
            if tile == '0':
                entities.append(RoadTile(x, y))
            elif tile == '1':
                entities.append(EmptyTile(x, y))

            x += 1

        y += 1
                

def reshape(w, h):
    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, w/h, 0.01, 50000)

last_display_timestamp = time.time()
def display():
    global last_display_timestamp
    global entities

    delta = time.time() - last_display_timestamp
    last_display_timestamp = time.time()

    glClearColor(0, 0, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glMatrixMode(GL_MODELVIEW)

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
