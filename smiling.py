import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    gluOrtho2D(-400, 400, -300, 300)
    glClearColor(0, 0, 0, 1)


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(2)

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1, 1, 0)
    for i in range(0, 361):
        theta = math.radians(i)
        x = 0 + 50 * math.cos(theta)
        y = 0 + 50 * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

    # Draw the first circle
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1, 0, 1)
    for i in range(0, 361):
        theta = math.radians(i)
        x = -20 + 10 * math.cos(theta)
        y = 10 + 10 * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

    # Draw the second circle
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1, 0, 1)
    for i in range(0, 361):
        theta = math.radians(i)
        x = 20 + 10 * math.cos(theta)
        y = 10 + 10 * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0, 0, 0)
    for i in range(180, 360, 1):
        theta = math.radians(i)
        x = 20 * math.cos(theta)
        y = -20 + 20 * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

    glFlush()


def main():
    glutInit(sys.argv)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(600, 0)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("CIRCLES")
    glutDisplayFunc(lambda: draw())
    init()
    glutMainLoop()


main()
