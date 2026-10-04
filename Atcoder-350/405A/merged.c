#include <stdio.h>

void read_abc(int *a, int *b, int *c) {
scanf("%d %d %d", a, b, c);
}

int compute_sum(int a, int b, int c) {
return a+b+c;
}

void print_ans(int x) {
printf("%d\n", x);
}

int main(void){ int a,b,c; read_abc(&a,&b,&c); int s=compute_sum(a,b,c); print_ans(s); return 0; }
