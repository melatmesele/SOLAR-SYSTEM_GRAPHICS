
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(45, 1, 0, 1, 50)
    gluLookAt(15, 15, 15, 0, 0, 0, 0, 1, 0)

    glEnable(GL_DEPTH_TEST)


def draw_solar(distance_from_sun, radius, rotation_angle, red, green, blue):
    glLoadIdentity()
    glColor(0.4, 0.35, 0.22)
    glutSolidTorus(0.01, distance_from_sun, 30, 30)
    glColor(red, green, blue)
    glRotate(rotation_angle, 0, 0, 1)
    glTranslate(distance_from_sun, 0, 0)
    glutSolidSphere(radius, 30, 30)


rotation_angle = [0, 0]


def show():

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    ##################### SUN ####################
    glColor(1.0, 1.0, 0.0)
    glutSolidSphere(1, 30, 30)

   ###################### Mercury ####################
    draw_solar(3, 0.5, rotation_angle[0], 1, 0, 0)
    rotation_angle[0] += 0.2

    ########################## VENUS ##################
    draw_solar(5, 0, 0.7, rotation_angle[1], 1, 0, 1)
    rotation_angle[1] += 0.3
    ########################## earth ##################
    draw_solar(7, 0, 0, 0.9, rotation_angle[2], 1, 0, 2)
    rotation_angle[2] += 0.4
    ########################## mars ##################
    draw_solar(5, 0,0,0, 0.11, rotation_angle[3], 1, 0, 3)
    rotation_angle[3] += 0.5
    ########################## jupiter ##################
    draw_solar(5, 0,0,0,0, 0.13, rotation_angle[4], 1, 0, 4)
    rotation_angle[4] += 0.6
    ########################## saturn ##################
    draw_solar(5, 0,0,0,0,0, 0.15, rotation_angle[5], 1, 0, 5)
    rotation_angle[5] += 0.7
    ########################## uranus ##################
    draw_solar(5, 0,0,0,0,0,0, 0.17, rotation_angle[6], 1, 0, 6)
    rotation_angle[6] += 0.8
    ########################## neptune ##################
    draw_solar(5, 0,0,0,0,0,0,0, 0.19, rotation_angle[7], 1, 0, 7)
    rotation_angle[7] += 0.9



    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(800, 800)
glutCreateWindow(b'Wire cube')
glutDisplayFunc(show)
glutIdleFunc(show)
init()
glutMainLoop()
