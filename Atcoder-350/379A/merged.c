#include <stdio.h>

void read_input(int *N){ scanf("%d", N); }

void extract_digits(int N,int *a,int *b,int *c){ *c=N%10; N/=10; *b=N%10; N/=10; *a=N%10; }

void build_numbers(int a,int b,int c,int *x,int *y){ *x=b*100+c*10+a; *y=c*100+a*10+b; }

void print_answer(int x,int y){ printf("%d %d\n", x,y); }

int main(void){ int N,a,b,c,x,y; read_input(&N); extract_digits(N,&a,&b,&c); build_numbers(a,b,c,&x,&y); print_answer(x,y); return 0; }
