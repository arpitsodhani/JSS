#include <stdio.h>
#include <string.h>

void read_ab(int *a, int *b) {
scanf("%d %d", a, b);
}

int decide(int a, int b) {
if(a>b) return 1; if(b>a) return 2; return 0;
}

void print_ans(int code) {
if(code==1) puts("A"); else if(code==2) puts("B"); else puts("equal");
}

int main(void){ int a,b; read_ab(&a,&b); int code=decide(a,b); print_ans(code); return 0; }
