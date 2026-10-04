#include <stdio.h>

int read_x(void) {
int x; scanf("%d", &x); return x;
}

int solve(int x) {
int total=0; for(int i=1;i<=9;i++) for(int j=1;j<=9;j++) total+=i*j;
int cnt=0; for(int i=1;i<=9;i++) for(int j=1;j<=9;j++) if(i*j==x) cnt++;
return total - cnt*x;
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ int x=read_x(); int ans=solve(x); print_int(ans); return 0;}
