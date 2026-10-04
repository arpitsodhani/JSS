#include <stdio.h>

int read_n(void) {
int n; scanf("%d", &n); return n;
}

int sign_nonzero(int n) {
return n>0?1:-1;
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ int n=read_n(); int s=sign_nonzero(n); print_int(s); return 0; }
