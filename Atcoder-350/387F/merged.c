#include <stdio.h>

void read_input(int *a,int *b,int *c) {
scanf("%d%d%d", a,b,c);
}

int calc(int a,int b,int c) {
return (a<=b && b<=c);
}

void print_int(int x) {
printf("%s\n", x?"Yes":"No");
}

int main(void){ int a,b,c; read_input(&a,&b,&c); int ans=calc(a,b,c); print_int(ans); return 0;}
