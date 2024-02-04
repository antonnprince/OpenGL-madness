from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

x = 0
y = 0
theta = 0


def init():
    gluOrtho2D(-400, 400, -400, 400)
    glClearColor(0, 0, 0, 1)


def circle(xt, yt):
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(3)
    glColor3f(1, 0, 1)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, 360, 1):
        xc = 30 * math.cos(math.radians(i)) + xt
        yc = 30 * math.sin(math.radians(i)) + yt
        glVertex2f(xc, yc)
    glEnd()
    glFlush()


def animate(value):
    global x, y, theta
    glutPostRedisplay()
    glutTimerFunc(int(1000 / 60), animate, 0)
    theta = theta + 1
    x = 40 * math.sin(math.radians(theta))
    y = -40 * math.cos(math.radians(theta))


def display():
    global x, y
    circle(x, y)


def main():
    glutInit(sys.argv)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("solar")
    glutDisplayFunc(display)
    glutTimerFunc(0, animate, 0)
    init()
    glutMainLoop()


main()
