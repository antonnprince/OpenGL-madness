from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

X = -400
Y = 100
A = -380
B = 80


def init():
    gluOrtho2D(-400, 400, -400, 400)
    glClearColor(0, 0, 0, 1)


def plane():
    glClear(GL_COLOR_BUFFER_BIT)
    global X, Y
    glLineWidth(3)
    glColor3f(0, 1, 0)
    glBegin(GL_QUADS)
    glVertex2f(X, Y)
    glVertex2f(X + 200, Y)
    glVertex2f(X + 100, Y + 50)
    glVertex2f(X, Y + 50)
    glEnd()
    glFlush()


def man():
    global A, B
    # glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(3)
    glColor3f(1, 1, 0)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(00, 180, 1):
        glVertex2f(
            A + (20) * math.cos(math.radians(i)),
            B + (20) * math.sin(math.radians(i)),
        )
    glEnd()
    glFlush()


def display():
    plane()
    man()


def animate(value):
    global X, A, B
    glutPostRedisplay()
    glutTimerFunc(500, animate, 0)
    if X < 400:
        X = X + 10
        A = A + 10
        B = B - 10
    else:
        X = 0


def main():
    glutInit(sys.argv)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(600, 0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("plane")
    glutDisplayFunc(display)
    glutTimerFunc(1000, animate, 0)
    init()
    glutMainLoop()


main()
