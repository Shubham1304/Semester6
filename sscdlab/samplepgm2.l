%{
#include<stdio.h>
int c=0;
%}
%%
[a] {c++;} ECHO;
%%
int main()
{
printf("Enter expression"); 
yylex(); ECHO;
printf("%d",c);
printf("%s",yylex());
}