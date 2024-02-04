from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

x_rotate = [0, 0, 0]
y_rotate = [350, 300, 200]  # s,m,h
length = [350, 300, 200]


def init():
    gluOrtho2D(-600, 600, -600, 600)
    glClearColor(1, 1, 1, 0)


def drawCirc(xc, yc, radius):
    theta = 0
    glColor3f(1, 0, 1)
    glBegin(GL_POINTS)
    for i in range(0, 361):
        theta = math.radians(i)
        x = radius * math.cos(theta) + xc
        y = radius * math.sin(theta) * yc
        glVertex2f(x, y)
    glEnd()


def drawHand(length, x, y):
    glLineWidth(5)
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(x, y)
    glEnd()


def clock():
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(5)
    glColor3f(1, 1, 0)
    drawCirc(0, 0, 400)
    for i in range(0, 3):
        drawHand(length[i], x_rotate[i], y_rotate[i])
    glutSwapBuffers()


def animate(value):
    glutPostRedisplay()
    glutTimerFunc(int(1000 / 60), animate, 0)
