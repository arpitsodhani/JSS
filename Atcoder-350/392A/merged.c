#include <stdio.h>

void read3(int *a,int *b,int *c) {
scanf("%d%d%d", a,b,c);
}

int check_perm(int a,int b,int c) {
if(a*b==c) return 1;
if(a*c==b) return 1;
if(b*c==a) return 1;
return 0;
}

void print_yesno(int x) {
printf("%s\n", x?"Yes":"No");
}

int main(void){ int a,b,c; read3(&a,&b,&c); int ok=check_perm(a,b,c); print_yesno(ok); return 0; }
