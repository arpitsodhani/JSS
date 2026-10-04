#include <stdio.h>
#include <stdlib.h>

int read_input(int *A) {
int n; scanf("%d", &n); for(int i=0;i<n;i++) scanf("%d", &A[i]); return n;
}

long long solve(int n,int *A) {
long long ans=0; for(int i=0;i<n;i++) ans+=A[i]*(long long)(i+1); return ans;
}

void print_ll(long long x) {
printf("%lld\n", x);
}

int main(void){ static int A[200005]; int n=read_input(A); long long ans=solve(n,A); print_ll(ans); return 0;}
