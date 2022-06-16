import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import numpy as np


def init():
    pygame.init()
    display = (630, 630)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)








def rotationMatrix(degree):
    radian = degree * np.pi / 180.0
    mat = np.array([
        [np.cos(radian), -np.sin(radian)],
        [np.sin(radian), np.cos(radian)],
    ])

    glClear(GL_COLOR_BUFFER_BIT)
    # y
    glBegin(GL_LINES)
    glColor3f(1.0, 3.0, 0.0)
    v = np.array([0.0, 6.0])
    po = np.array([0.0, 0.0])
    t = 1
    p = [po[0] + t * v[0], po[1] + t * v[1]]

    glVertex2f(0.0, 0.0)
    glVertex2f(p[0], p[1])

    glEnd()
    # -y
    glBegin(GL_LINES)
    glColor3f(1.0, 3.0, 0.0)
    v = np.array([0.0, -6.0])
    po = np.array([0.0, 0.0])
    t = 1
    p = [po[0] + t * v[0], po[1] + t * v[1]]

    glVertex2f(0.0, 0.0)
    glVertex2f(p[0], p[1])

    glEnd()
    # x
    glBegin(GL_LINES)
    glColor3f(1.0, 3.0, 0.0)
    v = np.array([6.0, 0.0])
    po = np.array([0.0, 0.0])
    t = 1
    p = [po[0] + t * v[0], po[1] + t * v[1]]

    glVertex2f(0.0, 0.0)
    glVertex2f(p[0], p[1])

    glEnd()
    # -x
    glBegin(GL_LINES)
    glColor3f(1.0, 2.0, 0.0)
    v = np.array([-6.0, 0.0])
    po = np.array([0.0, 0.0])
    t = 1
    p = [po[0] + t * v[0], po[1] + t * v[1]]

    glVertex2f(0.0, 0.0)
    glVertex2f(p[0], p[1])

    glEnd()


    glBegin(GL_LINES)
    glColor3f(1.0, 2.0, 0.0)
    v = np.array([0.1, 0.0])
    po = np.array([0.0, 0.2])
    t = 0.3
    p = [po[0] + t * v[0], po[1] + t * v[1]]

    x = np.array(np.dot([-0.3, 0.2], mat))
    y = np.array(np.dot([0.3,0.2], mat))
    glVertex2f(x[0], x[1])
    glVertex2f(y[0], y[1])
    glEnd()



    # 2 quadrant

    glBegin(GL_LINES)
    glColor3f(1.0, 2.0, 0.0)
    v = np.array([0.3, 0.0])
    po = np.array([0.0, 0.2])
    t = 1.0
    p = [po[0] + t * v[0], po[1] + t * v[1]]
    x = np.array(np.dot([0.3,-0.2], mat))
    y = np.array(np.dot(p, mat))
    glVertex2f(x[0], x[1])
    glVertex2f(y[0], y[1])

    glEnd()

    # nay tahti
    glBegin(GL_LINES)
    glColor3f(1.0, 2.0, 0.0)
    v = np.array([1.0, 0.0])
    po = np.array([0.0, -0.2])
    t = 0.3
    p = [po[0] + t * v[0], po[1] + t * v[1]]
    x = np.array(np.dot([-0.3, -0.2], mat))
    y = np.array(np.dot(p, mat))
    glVertex2f(x[0], x[1])
    glVertex2f(y[0], y[1])

    glEnd()


    glBegin(GL_LINES)
    glColor3f(1.0, 2.0, 0.0)
    v = np.array([-0.3, 0.0])
    po = np.array([0.0, 0.2])
    t = 1
    p = [po[0] + t * v[0], po[1] + t * v[1]]
    x = np.array(np.dot([-0.3, -0.2], mat))
    y = np.array(np.dot(p, mat))
    glVertex2f(x[0], x[1])
    glVertex2f(y[0], y[1])

    glEnd()

    glBegin(GL_LINES)
    glColor3f(1.0, 2.0, 0.0)
    v = np.array([0.1, 0.0])
    po = np.array([0.0, 0.2])
    t = 0.3
    p = [po[0] + t * v[0], po[1] + t * v[1]]

    x = np.array(np.dot([-0.7, 0.6], mat))
    y = np.array(np.dot([0.7,0.6], mat))
    glVertex2f(x[0], x[1])
    glVertex2f(y[0], y[1])
    glEnd()



    # 2 quadrant

    glBegin(GL_LINES)
    glColor3f(1.0, 2.0, 0.0)
    v = np.array([0.7, 0.0])
    po = np.array([0.0, 0.6])
    t = 1.0
    p = [po[0] + t * v[0], po[1] + t * v[1]]
    x = np.array(np.dot([0.7,-0.6], mat))
    y = np.array(np.dot(p, mat))
    glVertex2f(x[0], x[1])
    glVertex2f(y[0], y[1])

    glEnd()

    # nay tahti
    glBegin(GL_LINES)
    glColor3f(1.0, 2.0, 0.0)
    v = np.array([0.1, 0.0])
    po = np.array([0.0, -0.6])
    t = 0.7
    p = [po[0] + t * v[0], po[1] + t * v[1]]
    x = np.array(np.dot([-0.7, -0.6], mat))
    y = np.array(np.dot([0.7,-0.6], mat))
    glVertex2f(x[0], x[1])
    glVertex2f(y[0], y[1])

    glEnd()


    glBegin(GL_LINES)
    glColor3f(1.0, 2.0, 0.0)
    v = np.array([-0.7, 0.0])
    po = np.array([0.0, 0.6])
    t = 1
    p = [po[0] + t * v[0], po[1] + t * v[1]]
    x = np.array(np.dot([-0.7, -0.6], mat))
    y = np.array(np.dot(p, mat))
    glVertex2f(x[0], x[1])
    glVertex2f(y[0], y[1])

    glEnd()

    glFlush()



def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        rotationMatrix(60)
        pygame.display.flip()
        pygame.time.wait(10)


main()
