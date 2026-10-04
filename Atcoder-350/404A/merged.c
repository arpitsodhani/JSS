#include <stdio.h>

void read_ab(int *a, int *b) {
scanf("%d %d", a, b);
}

void print_range(int a, int b) {
for(int x=a;x<=b;x++) printf("%d\n", x);
}

int main(void){ int a,b; read_ab(&a,&b); print_range(a,b); return 0; }
