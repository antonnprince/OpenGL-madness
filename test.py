from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math


def init():
    gluOrtho2D(-300, 300, -300, 300)
    glClearColor(0, 0, 0, 1)


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(7)

    # First figure
    glColor3f(1, 0, 1)
    glBegin(GL_LINES)
    for i in range(70, 290):
        theta = math.radians(i)
        x = 100 * math.cos(theta)
        y = 100 * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

    # Second figure
    glColor3f(1, 0, 1)
    glBegin(GL_LINES)
    for i in range(70, 290):
        theta = math.radians(i)
        x = 100 * math.cos(theta)
        y = 100 * math.sin(theta) - 200
        glVertex2f(-x, y)
    glEnd()

    glFlush()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(600, 0)
    glutCreateWindow("S")
    glutDisplayFunc(lambda: draw())
    init()
    glutMainLoop()


main()
