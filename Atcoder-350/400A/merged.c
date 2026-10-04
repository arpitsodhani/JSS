#include <stdio.h>

int read_a(void) {
int a; scanf("%d", &a); return a;
}

int calc_b(int a) {
if(400%a!=0) return -1; return 400/a;
}

int main(void){ int a=read_a(); printf("%d\n", calc_b(a)); return 0; }
