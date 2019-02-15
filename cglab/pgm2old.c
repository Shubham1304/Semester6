//Pgm2 - Bresenham's Line Drawing Algorithm 
#include<stdio.h>
#include<stdlib.h>
#include<math.h>

/*Bresenham line - drawing procedure forf |m|<1.0 */

void lineBres(int x0,int y0,int xEnd,int yEnd)
{
	int dx = fabs(xEnd-x)) , dy=fabs(yEnd-y0);
	int p = 2*dy-dx;
	int twody = 2*dy, twodyminusdx = 2*(dy-dx);
	int x,y;
	/*Determine which endpoint to use as start position */
	if(x0>xEnd)
	{
		x=xEnd;
		y=yEnd;
		xEnd=x0;
	}
	else
	{
		x=x0;
		y=y0;
	}
	setPixel(x,y	);
	while(x<xEnd)
	{
		x++;
		if(p<0)
			p+=twody;
		else
		{
			y++;
			p+=twodyminusdx;
		}
		setPixel(x,y);
	}
}

void display()
{
	lineBres(x0,y0,xEnd,yEnd);
	glFlush();

}	

int main (int argc, char ** argv)
{
	int x0,y0,xEnd,yEnd;
	printf("Enter start and end points");
	scanf("%d%d%d%d",&x0,&xEnd,&y0,&yEnd);
	glutInit(&argc,argv);
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB|GLUT_DEPTH);
	glutInitWindowSize(500,500);
	glutCreateWindow("Pgm 2");
	glutDisplayFunc(display);
	//glEnable(GL_DEPTH_TEST);
	glClearColor(1,1,1,1);
	glutMainLoop();
	return 0;
}













































































