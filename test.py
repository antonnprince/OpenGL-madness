from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys
import random
from pygame import mixer

x = 0
y = 0
t = 0
tr = 1


def init():
    gluOrtho2D(-300, 300, -300, 300)
    glClearColor(0, 0, 0, 1)


def drawcirc(q):
    glColor3f(1, 0, 1)
    glLineWidth(2)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, 361, 1):
        glVertex2f(q + 20 * math.cos(math.radians(i)), 20 * math.sin(math.radians(i)))
    glEnd()

    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex2f(q + 20 * math.cos(math.radians(t)), 20 * math.sin(math.radians(t)))
    glVertex2f(q - 20 * math.cos(math.radians(t)), -20 * math.sin(math.radians(t)))
    glEnd()
    glutSwapBuffers()


def squ():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 1, 1)
    glLineWidth(3)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + 100, y)
    glVertex2f(x + 100, y + 60)
    glVertex2f(x, y + 60)
    glEnd()
    drawcirc(x + 10)
    drawcirc(x + 100)
    glutSwapBuffers()


def animate(value):
    glutPostRedisplay()
    global x, t
    if x < 500:
        x += 1
        t += 1
    else:
        x = 0
    glutTimerFunc(int(1000 / 60), animate, 0)


def main():
    global x
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(600, 0)
    glutCreateWindow("WHEELS")
    glutDisplayFunc(lambda: squ())
    glutTimerFunc(0, animate, 0)
    init()
    glutMainLoop()


main()
