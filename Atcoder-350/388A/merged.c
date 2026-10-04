#include <stdio.h>

void read_input(int *a,int *b) {
scanf("%d%d", a,b);
}

int calc(int a,int b) {
return a+b;
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ int a,b; read_input(&a,&b); int ans=calc(a,b); print_int(ans); return 0;}
