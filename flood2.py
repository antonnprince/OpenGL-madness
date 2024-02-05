from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import numpy as np

X = -300
Y = 100
WS = 500
PS = 5
sys.setrecursionlimit(1000000)


def init():
    gluOrtho2D(-400, 400, -400, 400)
    glClearColor(0, 0, 0, 1)


def get_pixel(x, y):
    pixel = glReadPixels(x, WS - y, 1, 1, GL_RGB, GL_FLOAT)
    return np.array([round(x, 1) for x in pixel[0][0]])


def set_pixel(x, y, fill_color=(0, 0, 0)):
    glColor3f(*fill_color)
    glPointSize(PS)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def flood(x, y, newcol, oldcol):
    color = get_pixel(x, y)
    if all(color == oldcol):
        set_pixel(x, y, newcol)
        flood(x + PS, y, newcol, oldcol)
        flood(x, y + PS, newcol, oldcol)
        flood(x - PS, y, newcol, oldcol)
        flood(x, y - PS, newcol, oldcol)


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(2)
    glColor3f(1, 0, 1)
    glBegin(GL_QUADS)
    glVertex2f(X, Y)
    glVertex2f(X + 50, Y)
    glVertex2f(X + 50, Y + 50)
    glVertex2f(X, Y + 50)
    glEnd()
    glutSwapBuffers()


def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        print(x, y)
        flood(x, y, [1, 1, 0], get_pixel(x, y))


def main():
    glutInit()
    glutInitWindowSize(WS, WS)
    glutCreateWindow("flood")
    glutDisplayFunc(draw)
    glutMouseFunc(mouse_click)
    glutMainLoop()
    inti()


main()
