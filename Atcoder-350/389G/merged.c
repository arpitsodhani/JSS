#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,long long *P) {
scanf("%d%lld", N,P);
}

void solve(int N,long long P,long long *out) {
int Mmin=N-1, Mmax=N*(N-1)/2; for(int m=Mmin;m<=Mmax;m++) out[m]=0;
}

void print_all(int N,long long P,long long *out) {
int Mmin=N-1, Mmax=N*(N-1)/2; for(int m=Mmin;m<=Mmax;m++) printf("%lld\n", out[m]%P);
}

int main(void){ int N; long long P; static long long out[500000]; read_input(&N,&P); solve(N,P,out); print_all(N,P,out); return 0;}
