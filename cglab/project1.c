#include<math.h>
#include<stdlib.h>
#include<stdio.h>




void mouse(int button, int state, int x, int y)
{
    if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN) {
        lmb = 1;
        oldx = x; oldy = y;
    }
    if (button == GLUT_LEFT_BUTTON && state == GLUT_UP) {
        lmb = 0;
    }
 
    if (button == GLUT_MIDDLE_BUTTON && state == GLUT_DOWN) {
        mmb = 1;
        oldx = x; oldy = y;
    }
    if (button == GLUT_MIDDLE_BUTTON && state == GLUT_UP) {
        mmb = 0;
    }

}


void motion(int x, int y)
{
    if (lmb) {
        ang += ((oldx - x) / 4.0 );
        scale += ((oldy - y) / 400.0);

        oldx = x; oldy = y;
        glutPostRedisplay();
    }
    if (mmb) {
        tx += ((float) (x - oldx)) / 500.0;
        ty += ((float) (oldy - y)) / 500.0;

        oldx = x; oldy = y;
        glutPostRedisplay();     
    }
}


void grab_screen(void)
{
    glCopyTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 0, 0, MAXSIZE, MAXSIZE,0);

    if (smooth) { glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
    }
else {
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    }
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE,  GL_DECAL);
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_FASTEST);
}

void redraw(void)
{
    glClear(GL_COLOR_BUFFER_BIT);          

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    glTranslatef(tx, ty, 0.0);
    glRotatef(ang, 0.0, 0.0, 1.0);
    glScalef(scale, scale, scale);

    if (autospin) {
        ang = 3.0 * cos(atime);
        scale = 1.0 + ( sin(atime / 4.0) * 0.1) ;
        atime += 0.01;
    }

    /* draw feedback square */
    glEnable(GL_TEXTURE_2D);
    glBegin(GL_QUADS);
        glTexCoord2f(0.0, 0.0); glVertex2f(-1.0, -1.0);
        glTexCoord2f(1.0, 0.0); glVertex2f(1.0, -1.0);
        glTexCoord2f(1.0, 1.0); glVertex2f(1.0, 1.0);
        glTexCoord2f(0.0, 1.0); glVertex2f(-1.0, 1.0);
    glEnd();
    glDisable(GL_TEXTURE_2D);
   
    /* draw square outline */
    glColor3f(1.0, 1.0, 1.0);
    glBegin(GL_LINE_LOOP);
        glVertex2f(-1.0, -1.0);
        glVertex2f(1.0, -1.0);
        glVertex2f(1.0, 1.0);
        glVertex2f(-1.0, 1.0);
    glEnd();
   
    /* seed pattern */
    glLoadIdentity();
    switch(seedmode) {
    case 0:
        seed();
        break;
    case 1:
        seed_circle();
        break;
    case 2:
        seed_teapot();
        break;
    case 3:
        seed_text(TEXT);
        break;
    }

void reset(void)
{
    ang = 0.0;
    scale = 1.0;
    tx = ty = 0.0;
    autospin = 0;

    glClear(GL_COLOR_BUFFER_BIT);
    grab_screen();

}

int main (int argc, char ** argv)
{
	glutInit(&argc,argv);
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB|GLUT_DEPTH);
	glutInitWindowSize(500,500);
	glutCreateWindow("3d Gasket");
	glutReshapeFunc(reset);
	glutDisplayFunc(redraw);
	glEnable(GL_DEPTH_TEST);
	glClearColor(1,1,1,1);
	glutMainLoop();
	return 0;	

}


































