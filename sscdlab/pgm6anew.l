%{
#include<stdio.h>
#include<stdlib.h>
int c1=0,c2=0;
%}
%x CMT

%%
"//".* {c1++;}
"/*" {BEGIN CMT;}
<CMT>. ;
<CMT>\n {c2++;}
<CMT>"*/" {c2++; BEGIN 0;}

%%
int main(int argc,char **argv)
{
  if (argc<2)
  {
    printf("Wrong input");
    exit(0);
  }
  yyin = fopen(argv[1],"r");
  yyout= fopen(argv[2],"w");
  yylex();
printf("comment lines:%d",c1+c2);
return 0;
}
