#include <stdio.h>

void read_input(int *n, unsigned long long *a) {
scanf("%d", n); for(int i=0;i<*n;i++) scanf("%llu", &a[i]);
}

long long mod_pow(long long a, long long e) {
const long long MOD=998244353LL; long long r=1%MOD; while(e){ if(e&1) r=r*a%MOD; a=a*a%MOD; e>>=1; } return r;
}

void basis_insert(unsigned long long *basis, unsigned long long x) {
for(int b=63;b>=0;b--){ if(((x>>b)&1ULL)==0ULL) continue; if(!basis[b]){ basis[b]=x; return; } x^=basis[b]; }
}

int compute_rank(int n, const unsigned long long *a, unsigned long long *basis) {
for(int i=0;i<64;i++) basis[i]=0; int rank=0; for(int i=0;i<n;i++){ unsigned long long x=a[i]; for(int b=63;b>=0;b--){ if(((x>>b)&1ULL)==0ULL) continue; if(!basis[b]){ basis[b]=x; rank++; break; } x^=basis[b]; } } return rank;
}

long long compute_answer(int n, int rank) {
const long long MOD=998244353LL; long long ways=mod_pow(2LL,(long long)n-rank); ways=(ways-1+MOD)%MOD; return ways;
}

void print_ans(long long x) {
printf("%lld\n", x);
}

int main(void){ int n; static unsigned long long a[200005]; unsigned long long basis[64]; read_input(&n,a); int r=compute_rank(n,a,basis); long long ans=compute_answer(n,r); print_ans(ans); return 0; }
