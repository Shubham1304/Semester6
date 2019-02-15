%{
#include<stdio.h>
#include<stdlib.h>
int yyerror();
int yyparse();
%}
%token A B
%%
S: A s1 B |B
s1: A s1| ;
%%
int yyerror()
{
  printf("error");
  exit(0);
}
int main()
{
  printf("Enter an expression\n");
  yyparse();
  printf("Successful grammar");
}
