from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys
import random
from pygame import mixer

mixer.init()
plays = mixer.Sound("horn.wav")

x = 0
y = 0
t = 0
tr = 1


def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-500, 500, -500, 500)


def drawcir(q):
    glColor3f(1, 1, 1)
    glLineWidth(2)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(q, 0)
    for i in range(0, 361, 1):
        glVertex2f(
            q + 20 * math.cos(math.pi * i / 180), 20 * math.sin(math.pi * i / 180)
        )
    glEnd()
    glColor3f(0, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(q + 20 * math.cos(t), 20 * math.sin(t))
    glVertex2f(q - 20 * math.cos(t), -20 * math.sin(t))
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(q - (20) * math.sin(t), (20) * math.cos(t))
    glVertex2f(
        q + (-20) * math.sin(t),
        (-20) * math.cos(t),
    )
    glEnd()


def draw():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 1, 0)
    glBegin(GL_QUADS)
    glVertex2f(x + 10, y)
    glVertex2f(x + 250, y)
    glVertex2f(x + 220, y + 30)
    glVertex2f(x, y + 50)
    glEnd()
    glBegin(GL_QUADS)
    glVertex2f(x, y + 30)
    glVertex2f(x + 20, y + 65)
    glVertex2f(x + 155, y + 60)
    glVertex2f(x + 180, y + 10)
    glEnd()
    drawcir(x + 50)
    drawcir(x + 200)
    glutSwapBuffers()


def animate(value):
    global x, y, t, tr, yr
    if tr == 1:
        if x < 500:
            x = x + 1
        else:
            x = -500
        if t > -math.radians(360):
            t -= 0.01
        else:
            t = 0.00
    elif tr == 0:
        if x > -500:
            x = x - 1
        else:
            x = 500
        if t < math.radians(360):
            t += 0.01
        else:
            t = 0.00
    elif tr == -1:
        pass
    glutPostRedisplay()
    glutTimerFunc(100, animate, 100)


def keyboard(key, x, y):
    global tr, yr
    key = key.decode()
    if key == "d":
        tr = 1
    elif key == "a":
        tr = 0
    elif key == "h":
        plays.play()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(600, 0)
    glutCreateWindow("CAR")
    glutDisplayFunc(lambda: draw())
    glutTimerFunc(0, animate, 0)
    glutKeyboardFunc(keyboard)
    init()
    glutMainLoop()


main()
