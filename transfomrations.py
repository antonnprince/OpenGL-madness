import math
import time
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    gluOrtho2D(-300, 300, -300, 300)
    glClearColor(0, 0, 0, 1)


def plotpolygon(sides):
    glClear(GL_COLOR_BUFFER_BIT)  # Reset the modelview matrix
    glLineWidth(2)
    glBegin(GL_LINES)
    for i in range(len(sides)):
        x1, y1 = sides[i]
        x2, y2 = sides[(i + 1) % len(sides)]
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
    glEnd()
    glFlush()


def drawtrans(sides, tx, ty):
    newsides = []
    for i in sides:
        newsides.append([i[0] + tx, i[1] + ty])
    glColor3f(1, 1, 1)
    plotpolygon(sides)  # Draw the original polygon
    glColor3f(1, 0, 1)
    plotpolygon(newsides)  # Draw the translated polygon
    # Swap the buffers after drawing both polygons


def drawscale(sides, tx, ty, px, py):
    newsides = []
    for i in sides:
        newsides.append([(i[0] - px) * tx + px, (i[1] - py) * ty + py])
    glColor3f(0, 0, 1)
    plotpolygon(newsides)
    glColor3f(1, 0, 1)
    plotpolygon(sides)
    glFlush()


def drawrotate(sides, tx, ty):
    newsides = []
    for i in sides:
        newsides.append(
            [
                round(
                    (i[0] - tx) * math.cos(theta) - (i[1] - ty) * math.sin(theta) + tx,
                    (i[0] - tx) * math.sin(theta)
                    + ((i[1] - ty) * math.cos(theta) + ty),
                )
            ]
        )


# Swap the buffers after drawing both polygons


def main():
    sides = [(30, 40), (50, 80), (70, 30)]
    glutInit(sys.argv)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(600, 0)
    glutInitDisplayMode(GLUT_RGBA)
    glutCreateWindow("SAMPLE")
    glutDisplayFunc(lambda: drawtrans(sides, 10, 10))
    init()
    glutMainLoop()


main()
