//Practise Pgm 1 - Outputing the line and points and triangle in the output screen

#include<GL/glut.h>

void init (void)
{
  glClearColor(1.0,1.0,1.0,0.0);
  glMatrixMode(GL_PROJECTION);
  gluOrtho2D(0.0,200.0,0.0,150.0);
}


void lineSegment(void)
{
  glClear(GL_COLOR_BUFFER_BIT);
  glLineWidth(100);
  glColor3f(1.0,0.0,0.0);
  //glBegin(GL_TRIANGLE_FAN);
  glBegin(GL_QUADS);
  //GL_QUAD_STRIP
  glVertex2i(180,15); //first vertex position from the bottom left position
  glVertex2i(10,145);
  glVertex2i(100,20);
  glVertex2i(190,20);
  //glVertex2i(30,30);
  glEnd();
  glFlush();
}

int main(int argc, char ** argv)
{
  glutInit(&argc,argv);
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
  glutInitWindowPosition(50,100);
  glutInitWindowSize(400,300);
  glutCreateWindow("An example");
  init();
  glutDisplayFunc(lineSegment);
  glutMainLoop();
}
