#include <stdio.h>

double read_x(void) {
double x; scanf("%lf", &x); return x;
}

int classify(double x) {
if(x>=38.0) return 1; if(x>=37.5) return 2; return 3;
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ double x=read_x(); int a=classify(x); print_int(a); return 0; }
