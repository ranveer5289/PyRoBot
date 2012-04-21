############################ 
#  Ranveer Raghuwanshi     #
#  200801077               #
############################

import sys
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame
import pygame.mixer

#initialize all imported pygame modules
pygame.init()


#Create a new Sound object from a file
sounds=pygame.mixer.Sound("man_sound.wav")


#Initializing Humanoid body parts
TORSO_RADIUS=0.1
TORSO_HEIGHT=0.4

UPPER_ARM_HEIGHT=0.2
UPPER_ARM_WIDTH=0.03

LOWER_ARM_HEIGHT=0.2
LOWER_ARM_WIDTH=0.05

UPPER_LEG_HEIGHT=0.2
UPPER_LEG_WIDTH=0.08

LOWER_LEG_HEIGHT=0.2
LOWER_LEG_WIDTH=0.06

SHOLDER_WIDTH = 0.2
HIP_WIDTH = 0.2

#X-axis position of head.
HEADX=0.1
HEADY=TORSO_HEIGHT

Left_Upper_Arm_X= - TORSO_RADIUS
Right_Upper_Arm_X = TORSO_RADIUS
Left_Upper_Arm_Y=Right_Upper_Arm_Y=TORSO_HEIGHT
Left_Left_Arm_Y=Right_Left_Arm_Y=LOWER_ARM_HEIGHT

Left_Upper_Leg_X=-1.0 * HIP_WIDTH / 2
Right_Upper_Leg_X=HIP_WIDTH / 2
Left_Upper_Leg_Y=Right_Upper_Leg_Y=0
Left_Lower_Leg_Y=Right_Lower_Leg_Y=LOWER_LEG_HEIGHT
angle = 0
t0=0.0
t1=0.0
t2=0.0
t3=90.0
t4=0.0
t5=90.0
t6=0.0
t7=180.0
t8=0.0
t9=180.0
t10=0.0
x1=2
y1=2
z1=2
x2,z2=0,0
y2=1

def changeView(eyex,eyey,eyez,upX,upY,upZ):
        gluLookAt(eyex, eyey, eyez, 0.0, 0.0, 0.0, upX, upY, upZ)



def display():
  global angle


  #clear buffers to preset values
  #Masks to be cleared.
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

  #specify which matrix is the current matrix. Currently MODELVIEW Matrix selected.
  #Used in relation to view and camera.
  glMatrixMode(GL_MODELVIEW)
  
  #TORSO
  #replace the current matrix with the identity matrix.Identity matrix resets
  #projection/model view matrix to its default state.
  glLoadIdentity()

  #define a viewing transformation
  #gluLookAt(2.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
  #changeView(2.0,2.0,2.0)
  changeView(x1,y1,z1,x2,y2,z2)
  glTranslatef(0,0,angle)
  
  #t0 Specifies the angle of rotation.
  glRotatef(t0, 0.0, 1.0, 0.0)
  gray()
  torso()
  glPushMatrix()

  #HEAD
  Pink()
  #Specify the x, y, and z coordinates of a translation vector.
  glTranslatef(0.0, HEADX, 0.0)
  glRotatef(t1, 1.0, 0.0, 0.0)
  glRotatef(t2, 0.0, 1.0, 0.0)
  glTranslatef(0.0, HEADY, 0.0)
  head()

  #LEFT UPPER ARM
  glPopMatrix()
  glPushMatrix()
  green()
  glTranslatef(Left_Upper_Arm_X, Left_Upper_Arm_Y, 0.0)
  glRotatef(t3, 1.0, 0.0, 0.0)
  upper_arm()

  #LEFT LOWER ARM
  pink()
  glTranslatef(0.0, Left_Left_Arm_Y, 0.0)
  glRotatef(t4, 1.0, 0.0, 0.0)
  lower_arm()

  #RIGHT UPPER ARM
  glPopMatrix()
  glPushMatrix()
  green()
  glTranslatef(Right_Upper_Arm_X, Right_Upper_Arm_Y, 0.0)
  glRotatef(t5, 1.0, 0.0, 0.0)
  upper_arm()

  #RIGHT LOWER ARM
  pink()
  glTranslatef(0.0, Right_Left_Arm_Y, 0.0)
  glRotatef(t6, 1.0, 0.0, 0.0)
  lower_arm()

  #LEFT UPPER LEG
  glPopMatrix()
  glPushMatrix()
  red()
  glTranslatef(Left_Upper_Leg_X, Left_Upper_Leg_Y, 0.0)
  glRotatef(t7, 1.0, 0.0, 0.0)
  upper_leg()

  #LEFT LOWER LEG
  blue()
  glTranslatef(0.0, Left_Lower_Leg_Y, 0.0)
  glRotatef(t8, 1.0, 0.0, 0.0)
  lower_leg()

  #RIGHT UPPER LEG
  glPopMatrix()
  glPushMatrix()
  red()
  glTranslatef(Right_Upper_Leg_X, Right_Upper_Leg_Y, 0.0)
  glRotatef(t9, 1.0, 0.0, 0.0)
  upper_leg()

  #RIGHT LOWER LEG
  blue()
  glTranslatef(0.0, Right_Lower_Leg_Y, 0.0)
  glRotatef(t10, 1.0, 0.0, 0.0)
  lower_leg()

  glPopMatrix()
  glFlush()

def torso():
  glPushMatrix()
  glRotatef(-90.0, 1.0, 0.0, 0.0)
  #Draw Cylinder.
  gluCylinder(p, TORSO_RADIUS, TORSO_RADIUS, TORSO_HEIGHT, 100, 100)
  glPopMatrix()

def head():
  glPushMatrix()
  glRotatef(90, 1.0, 0.0, 0.0)
  glutWireSphere(0.1, 100, 100)
  glPopMatrix()
  
def upper_arm():
  glPushMatrix()
  glTranslatef(0.0, 0.5*UPPER_ARM_HEIGHT, 0.0)
  glScalef(UPPER_ARM_WIDTH, UPPER_ARM_HEIGHT, UPPER_ARM_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

def lower_arm():
  glPushMatrix()
  glTranslatef(0.0, 0.5*UPPER_ARM_HEIGHT, 0.0)
  glScalef(LOWER_ARM_WIDTH, LOWER_ARM_HEIGHT, LOWER_ARM_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

def upper_leg():
  glPushMatrix()
  glTranslatef(0.0, 0.5*LOWER_ARM_HEIGHT, 0.0)
  glScalef(UPPER_LEG_WIDTH, UPPER_LEG_HEIGHT, UPPER_LEG_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()

def lower_leg():
  glPushMatrix()
  glTranslatef(0.0, 0.5*LOWER_ARM_HEIGHT, 0.0)
  glScalef(LOWER_LEG_WIDTH, LOWER_LEG_HEIGHT, LOWER_LEG_WIDTH)
  glutSolidCube(1.0)
  glPopMatrix()
  
def red():
  glColor3f(1.0, 0.0, 0.0)

def green():
  glColor3f(0.0, 1.0, 0.0)

def blue():
  glColor3f(0.0, 0.0, 1.0)

def cyan():
  glColor3f(0.0, 1.0, 1.0)


#change head/leg color.
def Pink():
  glColor3f(1.5, 0.5, 0.5)

def pink():
  glColor3f(1, 0, 1)

#change torso color.
def gray():
  glColor3f(0.2, 0.2, 0.2)
  
def mykey(key, x, y):
  global t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, angle,x1,y1,z1,x2,y2,z2
  if key=='d': # TORSO
    t0 = t0 + 10.0
    sounds.play() 
  elif key=='D':
    t0 = t0 - 10.0
    sounds.play() 
  elif key=='e': # HEAD 1
    t1 = t1 + 10.0
    sounds.play() 
  elif key=='E':
    t1 = t1 - 10.0
    sounds.play() 
  elif key=='r': # HEAD 2
    t2 = t2 + 10.0
    sounds.play() 
  elif key=='R':
    t2 = t2 - 10.0
    sounds.play() 
  elif key=='s': # LUA
    t3 = t3 + 10.0
    sounds.play() 
  elif key=='S':
    t3 = t3 - 10.0
    sounds.play() 
  elif key=='a': # LLA
    t4 = t4 + 10.0
    sounds.play() 
  elif key=='A':
    t4 = t4 - 10.0
    sounds.play() 
  elif key=='f': # RUA
    t5 = t5 + 10.0
    sounds.play() 
  elif key=='F':
    t5 = t5 - 10.0
    sounds.play() 
  elif key=='g': # RLA
    t6 = t6 + 10.0
    sounds.play() 
  elif key=='G':
    t6 = t6 -10.0
    sounds.play() 
  elif key=='x': # LUL
    t7 = t7 + 10.0
    sounds.play() 
  elif key=='X':
    t7 = t7 - 10.0
    sounds.play() 
  elif key=='z': # LLL
    t8 = t8 + 10.0
    sounds.play() 
  elif key=='Z':
    t8 = t8 -10.0
    sounds.play() 
  elif key=='c': # RUL
    t9 = t9 + 10.0
    sounds.play() 
  elif key=='C':
    t9 = t9 - 10.0
    sounds.play() 
  elif key=='v': # RLL
    t10 = t10 + 10.0
    sounds.play() 
  elif key=='V':
    t10 = t10 - 10.0
    sounds.play() 

  #Change Viewing(eye) angle. Move away from user if `u` key is pressed.
  elif key=='u':
          x1,y1,z1=x1+1,y1+1,z1+1
  #Move closer to user if 'U' is pressed.
  elif key=='U':
          x1,y1,z1=x1-1,y1-1,z1-1

  elif key=='j':
          x2=x2+1
  elif key == 'J':
          x2=x2-1

  elif key=='l':
          z2=z2+1
  elif key=='L':
          z2=z2-1

  elif key=='t':
    angle += 1
    sounds.play() 
  elif key=='q':
    sys.exit()


  print "params: ", t0, t1, t2, t3, t4, t5, t6, t7, t8, t9,t10,x1,y1,z1,x2,y2,z2
  glutPostRedisplay()
sounds.play()   
glutInit( sys.argv )
glutInitDisplayMode( GLUT_SINGLE | GLUT_RGB )
glutInitWindowSize( 500, 500 )
glutInitWindowPosition(0,0)
glutCreateWindow( 'Rubber Man' )
glutDisplayFunc( display )
glutKeyboardFunc(mykey)
p=gluNewQuadric()
gluQuadricDrawStyle(p, GLU_LINE)

glClearColor(0.0, 0.0, 0.0, 0.0)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(30, 1.0, 0.0, 100.0)

glutMainLoop()
