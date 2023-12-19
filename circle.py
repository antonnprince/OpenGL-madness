import math
import time
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    gluOrtho2D(-300, 300, -300, 300)
    glClearColor(0, 0, 0, 1)


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(2)
    glColor3f(1, 0, 1)
    glBegin(GL_TRIANGLE_FAN)
    """glVertex2f(40, 0)"""
    for i in range(0, 361):
        glVertex2f(50 * math.cos(i), 50 * math.sin(i))
    glEnd()
    glFlush()


def main():
    glutInit(sys.argv)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(600, 0)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("CIRCLE")
    glutDisplayFunc(lambda: draw())
    init()
    glutMainLoop()


main()
