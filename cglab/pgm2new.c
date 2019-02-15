#include <GL/glut.h>
#include <stdio.h>
#include <math.h>
int x0,xn,yi,ye;
void myInit() {
	glClear(GL_COLOR_BUFFER_BIT);
	glClearColor(0.0, 0.0, 0.0, 1.0);
	glMatrixMode(GL_PROJECTION);
	gluOrtho2D(0, 500, 0, 500);
}
void setpixel(int x, int y) {
	glBegin(GL_POINTS);
	glVertex2i(x, y);
	glEnd();
}
void bresenham_line(int x0, int xn, int y0, int yn) {
	int dx, dy, i, p;
	int e1, e2;
	int x,y;
	dx = fabs(xn-x0);
	dy = fabs(yn-y0);
if (dx > dy)
{
	if (x0 > xn)
	{
	x = xn; y = yn;
	xn=x0;
	}
	else
	{
	x = x0; y = y0;
	}
	setpixel(x, y);
		p = 2 * dy-dx;
		e1 = 2*(dy-dx);
		e2 = 2*dy;
		while(x<xn)
		{
			x++;
			if (p < 0)
				p += e2;
			else
			{
				y ++;
				p += e1;
			}
			setpixel(x, y);
		}
	}
else {
		if (y0 > yn)
		{
		x = xn; y = yn;
		yn=y0;
		}
		else
		{ 	x = x0; y = y0;
}
		setpixel(x, y);
		p = 2*dx-dy;  e1 = 2*(dx-dy);   e2 = 2*dx;
		while(y<yn)
		{
			if (p >= 0) {
				x ++; 	p += e1;
			}
			else
				p += e2;
y ++; 		setpixel(x, y);
		}
	}
}
void Display() {
	bresenham_line(x0, xn, yi, ye);
	glFlush();
}
void main(int argc, char **argv) {
	printf( "Enter (x0, y0, xend, yend)\n");
	scanf("%d%d%d%d", &x0, &yi, &xn, &ye);
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
	glutInitWindowSize(500, 500);
	glutInitWindowPosition(0, 0);
	glutCreateWindow("Bresenham's Line Drawing");
	myInit();
	glutDisplayFunc(Display);
	//glutMainLoop();
}
