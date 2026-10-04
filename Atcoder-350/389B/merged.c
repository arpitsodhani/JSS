#include <stdio.h>

long long read_x(void) {
long long x; scanf("%lld", &x); return x;
}

int find_n(long long x) {
long long f=1; int n=1; while(f<x){ n++; f*=n; } return n;
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ long long x=read_x(); int n=find_n(x); print_int(n); return 0;}
