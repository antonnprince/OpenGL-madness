from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

x_rotate = [0, 0, 0]
y_rotate = [350, 300, 200]  # s,m,h
length = [350, 300, 200]
theta = [0, 0, 0]


def init():
    gluOrtho2D(-600, 600, -600, 600)
    glClearColor(1, 1, 1, 0)


def drawCirc(xc, yc, radius):
    theta = 0
    glColor3f(1, 0, 1)
    glBegin(GL_POINTS)
    for i in range(0, 360):
        theta = math.radians(i)
        x = radius * math.cos(i)
        y = radius * math.sin(i)
        glVertex2f(x, y)
    glEnd()


def drawHand(x, y):
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
        drawHand(x_rotate[i], y_rotate[i])
    glutSwapBuffers()


def animate(value):
    glutPostRedisplay()
    glutTimerFunc(int(1000 / 60), animate, 0)
    for i in range(0, 3):
        x_rotate[i] = length[i] * math.sin(math.radians(theta[i]))
        y_rotate[i] = length[i] * math.cos(math.radians(theta[i]))
    if theta[0] > 360:
        theta[0] = 0
        theta[1] += 1
    else:
        theta[0] += 0.098

    if theta[1] > 360:
        theta[1] = 0
        theta[2] += 1

    if theta[2] >= 360:
        theta[2] = 0


def main():
    glutInit(sys.argv)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("clock")
    glutDisplayFunc(clock)
    glutTimerFunc(0, animate, 0)
    init()
    glutMainLoop()


main()
