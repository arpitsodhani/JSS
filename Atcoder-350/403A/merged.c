#include <stdio.h>

void read_abc(int *a, int *b, int *c) {
scanf("%d %d %d", a, b, c);
}

int can_reach(int a, int b, int c) {
int d=c-a; if(d<0) d=-d; if(b==0) return (a==c);
int r=d%b; return r==0;
}

void print_yesno(int ok) {
puts(ok?"Yes":"No");
}

int main(void){ int a,b,c; read_abc(&a,&b,&c); int ok=can_reach(a,b,c); print_yesno(ok); return 0; }
