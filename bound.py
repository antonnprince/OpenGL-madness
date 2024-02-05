from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys

ws = 800
point_size = 2
filclr = [0, 0, 1]


def get_pixel(x, y):
    data = glReadPixels(x, ws - y, 1, 1, GL_RGB, GL_FLOAT)
    return [round(x, 1) for x in data[0][0]]


def set_pixel(x, y, fill_color=(0, 0, 0)):
    glColor3f(*fill_color)
    glPointSize(point_size)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def plot_rect():
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    gluOrtho2D(0, ws, ws, 0)
    glColor3f(1, 0, 0)
    glLineWidth(point_size)

    sqrsize = 200
    xc = ws / 2
    yc = ws / 2
    hf = sqrsize / 2

    glBegin(GL_POLYGON)
    glVertex2f(xc - hf, yc - hf)
    glVertex2f(xc + hf, yc - hf)
    glVertex2f(xc + hf, yc + hf)
    glVertex2f(xc - hf, yc + hf)
    glEnd()
    glFlush()


def boundary_fill(x, y, fill_color, boundary_color):
    stack = [(x, y)]

    while stack:
        cx, cy = stack.pop()

        if cx >= 0 and cx < ws and cy >= 0 and cy < ws:
            color = get_pixel(cx, cy)

            if (color != fill_color) and (color != boundary_color):
                set_pixel(cx, cy, fill_color)

                stack.append((cx + point_size, cy))
                stack.append((cx, cy + point_size))
                stack.append((cx - point_size, cy))
                stack.append((cx, cy - point_size))


def mouse_click(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        boundary_fill(x, y, filclr, [1, 0, 0])


glutInit()
glutInitWindowSize(ws, ws)
glutCreateWindow("boundary-fill")
glutDisplayFunc(plot_rect)
glutMouseFunc(mouse_click)
glutMainLoop()
