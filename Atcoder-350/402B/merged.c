#include <stdio.h>

void read_nmk(int *n, int *m, int *k) {
scanf("%d %d %d", n, m, k);
}

long long nCk(int n, int k) {
if(k<0||k>n) return 0;
if(k>n-k) k=n-k;
__int128 num=1, den=1;
for(int i=1;i<=k;i++){ num*= (n-k+i); den*= i; }
return (long long)(num/den);
}

long long fact(int n) {
__int128 f=1; for(int i=2;i<=n;i++) f*=i; return (long long)f;
}

long long solve_count(int n, int m, int k) {
if(k>n||k>m) return 0;
long long a=nCk(n,k);
long long b=nCk(m,k);
long long c=fact(k);
__int128 res=(__int128)a*b*c;
return (long long)res;
}

void print_ll(long long x) {
printf("%lld\n", x);
}

int main(void){ int n,m,k; read_nmk(&n,&m,&k); long long ans=solve_count(n,m,k); print_ll(ans); return 0; }
