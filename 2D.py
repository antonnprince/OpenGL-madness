from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

x = 100
y = 300


def init():
    gluOrtho2D(-150, 250, -150, 250)  # Adjust viewport to fit the quad
    glClearColor(1, 0, 0, 1)


def draw():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)
    glLineWidth(2)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + 50, y)
    glVertex2f(x + 50, y + 50)
    glVertex2f(x, y + 50)
    glEnd()
    glutSwapBuffers()  # Use glFlush instead of glutSwapBuffers in single-buffered context


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(600, 0)
    glutCreateWindow("QUAD")
    glutDisplayFunc(lambda: draw())
    init()
    glutMainLoop()


main()
