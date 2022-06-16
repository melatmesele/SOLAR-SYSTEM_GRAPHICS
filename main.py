
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

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(800, 800)
glutCreateWindow(b'Wire cube')
glutDisplayFunc(show)
glutIdleFunc(show)
init()
glutMainLoop()
