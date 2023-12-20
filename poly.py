from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

X = -200
Y = 0


def init():
    gluOrtho2D(-300, 300, -300, 300)
    glClearColor(0, 0, 0, 1)


def draw(coordinate_list):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 1)
    glLineWidth(2)
    glBegin(GL_POLYGON)
    for i in coordinate_list:
        glVertex2f(*i)
    glEnd()
    glutSwapBuffers()


def main():
    n = int(input("Enter number of sides"))
    sides = []
    for i in range(1, n + 1):
        x = int(input("Enter x coordinate: "))
        y = int(input("Enter y coordinate: "))
        sides.append([x, y])
    glutInit(sys.argv)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(600, 0)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("N SIDED POLYGON")
    glutDisplayFunc(lambda: draw(sides))
    init()
    glutMainLoop()


main()
