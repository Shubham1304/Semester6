%{
#include<stdio.h>
#include<stdlib.h>
%}
%token a b
%%
input: S '\n' {printf ("Successful Grammar\n"); exit(0);}
S:a s1 b | b
s1: ; | a s1
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
}
