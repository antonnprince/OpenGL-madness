from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
X = -200
Y = 0

def init():
    gluOrtho2D(-300,300,-300,300)
    glClearColor(0,0,0,1)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLineWidth(2)
    glColor3f(1,0,1)
    glBegin(GL_QUADS)
    glVertex2f(X,Y)
    glVertex2f(X+50,Y)
    glVertex2f(X+50,Y+50)
    glVertex2f(X,Y+50)
    glEnd()
    glutSwapBuffers()

"""
def animate():

