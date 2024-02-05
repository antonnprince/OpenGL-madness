from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import numpy as np

X = -200
Y = 100
ws = 500
ps = 5
fillscol = [0, 0, 1]


def get_pixel(x, y):
    pixel = glReadPixels(x, ws - y, 1, 1, GL_RGB, GL_FLOAT)
    return np.array([round(x, 1) for x in pixel[0][0]])


def set_pixel(x, y, fillcol=(0, 0, 0)):
    glColor3f(*fillcol)
    glPointSize(ps)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def draw():
    global X, Y
    # glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(2)
    glColor3f(1, 0, 1)
    glBegin(GL_LINES)
    glVertex2f(-200, 0)
    glVertex2f(100, 0)
    glVertex2f(100, 50)
    glVertex2f(-200, 50)
    glEnd()
    glFlush()


def bound(x, y, fillcol, boundcol):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()

        if cx >= 0 and cx < ws and cy >= 0 and cy < ws:
            color = get_pixel(cx, cy)

            if (color != fillcol) and (color != boundcol):
                set_pixel(x, y, fillcol)
                stack.append((cx + ps, cy))
                stack.append((cx, cy + ps))
                stack.append((cx - ps, cy))
                stack.append((cx, cy - ps))


def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        bound(x, y, fillscol, [1, 0, 1])


glutInit()
glutInitWindowSize(ws, ws)
glutCreateWindow("boundary-fill")
glutDisplayFunc(draw)
glutMouseFunc(mouse_click)
glutMainLoop()
