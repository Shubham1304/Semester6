/* this is a comment */
%{
#include<stdio.h>
int v=0,op=0,id=0,flag=0,cons=0;
%}
%%
[A-Za-z]+ {id++; printf("\nIdentifier:"); ECHO;}
[0-9]+ {cons++; printf("\nConstant:"); ECHO;}
[\+\-\*\^\/=] {op++; printf("\nOperator"); ECHO;}

"(" {v++;}
")" {v--;}
";" {flag=1;}
.|\n {;}
%%
int main ()
{
printf("Enter expression");
yylex();
if((op+1)==(id+cons) && v==0 && flag==0)
	printf ("Valid Expression");
else
	printf("Invalid\n");
printf("No of operands=%d\n",id+cons);
printf("No of operators=%d\n",op);
return 1;
}
