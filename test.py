from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

x = 200
y = 300


def init():
    gluOrtho2D(-300, 300, -300, 300)
    glClearColor(0, 0, 0, 1)


def plotpolygon(sides):
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(2)
    glColor3f(1, 0, 1)
    glBegin(GL_LINES)
    for i in range(len(sides)):
        x1, y1 = sides[i]
        x2, y2 = sides[(i + 1) % len(sides)]
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
    glEnd()
    glFlush()


def trans(sides, tx, ty):
    newsides = []
    for i in sides:
        newsides.append(i[0] + tx, i[1] + ty)
    glColor3f(1, 1, 1)
