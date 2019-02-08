%{
#include<stdio.h>
int c=0,w=0,s=0,l=0;
%}
WORD [^ \t\n,\.:]+
EOL [\n]
%%
{WORD} {w++; c=c+yyleng;}
[ ] s++;
{EOL} {l++;}
. {c++;}
%%
int yywrap()
{
return 1;
}
int main(int argc,char *argv[])
{
	if(argc!=2)
	{
		printf("Usage <./a.out><sourcefile>\n");
		exit(0);
	}
	yyin = fopen (argv[1],"r");
	yylex();
	printf("No of characters%d\n",c);
	printf("No of words%d\n",w);
	printf("No of end of line%d\n",l);
	printf("No of spaces%d\n",s);
}