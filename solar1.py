import pygame
import numpy as np
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import tkinter as tk
from tkinter import *
root  = tk.Tk()
root.geometry("600x600")
def show():
    label.config( text = clicked.get())
    label.config(text=clicked1.get())

options = [
    "floor" ,  "logarithmic"  , "cubic" , "cos" , "sin" , "tan"
]
options1 = [
    "floor" ,  "logarithmic"  , "cubic" , "cos" , "sin" , "tan"
]

clicked = StringVar()
clicked1 = StringVar()
label= Label(root , text = " Choose the following drop downs. ")
label.pack()
drop = OptionMenu( root , clicked , *options)
drop.pack()
drop1 = OptionMenu( root , clicked1 , *options1)
drop1.pack()
button = Button(root , text = "Plot" , command = root.destroy).pack()
root.mainloop()
def init():
    pygame.init()
    display = (600 ,600)
    pygame.display.set_mode(display , DOUBLEBUF|OPENGL)
    glClearColor(0.0 , 0.0 ,0.0 , 1.0)
    gluOrtho2D(-5.0 , 5.0 , -5.0 , 5.0)
def origin():
    a = np.linspace(-1, 0.5, 500)
    b = np.linspace(1, 0.5, 500)
    glColor3f(1.0, 1.0, 1.0)
    y = np.linspace(-10, 10, 2000)
    yy = y-y
    x = np.linspace(-10, 10, 2000)
    xx = x-x
    glBegin(GL_LINE_STRIP)
    glColor3f(250, 250, 250)
    for a, b in zip (x,xx):
        glVertex2f(a, b)
    for a, b in zip (yy,y):
        glVertex2f(a, b)
    glEnd()
    glFlush()
def floor():
    x = np.linspace(-5, 5, 1500)
    y = np.floor(x)
    glBegin(GL_LINE_STRIP)
    glColor3f(55, 155, 0)
    for a, b in zip (x,y):
        glVertex2f(a, b)
    glEnd()
def logarithmic():
    # glClear(GL_COLOR_BUFFER_BIT)
    a = np.linspace(-1, 0.5, 500)
    b = np.linspace(1, 0.5, 500)
    x = np.linspace(-3, 6 , 1000)
    l = np.log(x)
    glBegin(GL_LINE_STRIP)
    glColor3f(0.0 , 0.0 , 1.0)
    for a ,b  in zip(x ,l):
        glVertex2f(a ,b)
    glEnd()
def cubic():
    a = np.linspace(-1, 0.5, 1000)
    b = np.linspace(1, 0.5, 1000)
    x = np.linspace(-8 , 8 ,1000)
    w = np.power(x ,3)
    glBegin(GL_LINE_STRIP)
    glColor3f(255 , 255 , 0.0)
    for a ,b  in zip (x ,w):
        glVertex2f(a ,b)
    glEnd()
def cos():
    a = np.linspace(-1, 0.5, 1000)
    b = np.linspace(1, 0.5, 1000)
    glColor3f(0.7 , 1.0 , 0.4)
    x = np.linspace(-3*np.pi, 3*np.pi, 300)
    u = np.cos(x)
    glPointSize(10)
    glBegin(GL_LINE_STRIP)
    for a ,b  in zip(x ,u):
        glVertex2f(a ,b)
    glEnd()
    glFlush()
def sin():
    a = np.linspace(-1, 0.5, 1000)
    b = np.linspace(1, 0.5, 1000)
    glColor3f(0.9 , 0.3 , 0.1)
    x = np.linspace(-3*np.pi, 3*np.pi, 300)
    y = np.sin(x)
    glPointSize(10)
    glBegin(GL_LINE_STRIP)
    for a ,b  in zip(x ,y):
        glVertex2f(a ,b)
    glEnd()
    glFlush()
def tan():
    a = np.linspace(-1, 0.5, 1000)
    b = np.linspace(1, 0.5, 1000)
    glColor3f(0.4, 1.0 , 1.1)
    x = np.linspace(-3*np.pi, 3*np.pi, 300)
    y = np.tan(x)
    # glPointSize(10)
    glBegin(GL_LINE_STRIP)
    for a ,b  in zip(x ,y):
        glVertex2f(a ,b)
    glEnd()
    glFlush()
def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if clicked.get() == options[0] or clicked1.get() == options1[0]:
            floor()
        if clicked.get() == options[1] or clicked1.get() == options1[1]:
            logarithmic()
        if clicked.get() == options[2] or clicked1.get() == options1[2] :
            cubic()
        if clicked.get() == options[3] or (clicked1.get() == options1[3]) :
            cos()
        if clicked.get() == options[4] or clicked1.get() == options1[4] :
            sin()
        if clicked.get() == options[5] or clicked1.get() == options1[5] :
            tan()
        origin()
        pygame.display.flip()
        pygame.time.wait(10)
main()