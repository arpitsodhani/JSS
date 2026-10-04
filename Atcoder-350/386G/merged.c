#include <stdio.h>

void read_input(int *N,long long *M) {
scanf("%d%lld", N,M);
}

long long solve(int N,long long M) {
return 0;
}

void print_ll(long long x) {
printf("%lld\n", x%998244353LL);
}

int main(void){ int N; long long M; read_input(&N,&M); long long ans=solve(N,M); print_ll(ans); return 0;}
