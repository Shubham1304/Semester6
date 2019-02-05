%{
	#include<stdio.h>
	int vowels=0,cons=0;
%}
%%
[aeiouAEIOU] {vowels++;}
[a-zA-Z] {cons++;}
%%
int yywrap()
{	
return 1; 
}
int main()
{
printf("Enter the string \n");
yylex();
printf("No of vowels=%d",vowels);
printf("No of consonants=%d",cons);
return 1;
}
