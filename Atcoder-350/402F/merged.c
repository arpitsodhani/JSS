#include <stdio.h>
#include <stdlib.h>

void read_input(int *n, long long *a) {
scanf("%d", n); for(int i=0;i<*n;i++) scanf("%lld", &a[i]);
}

unsigned long long squarefree_hash(long long x) {
unsigned long long h=0;
long long t=x;
for(long long p=2;p*p<=t;p+=(p==2?1:2)){
  int e=0;
  while(t%p==0){ t/=p; e^=1; }
  if(e){
    unsigned long long z=(unsigned long long)p + 0x9e3779b97f4a7c15ULL;
    z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
    z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
    z = z ^ (z >> 31);
    h ^= z;
  }
}
if(t>1){
  unsigned long long z=(unsigned long long)t + 0x9e3779b97f4a7c15ULL;
  z = (z ^ (z >> 30)) * 0xbf58476d1ce4e5b9ULL;
  z = (z ^ (z >> 27)) * 0x94d049bb133111ebULL;
  z = z ^ (z >> 31);
  h ^= z;
}
return h;
}

long long count_square_subseq(int n, const long long *a) {
const long long MOD=998244353LL;
unsigned long long basis[64]; for(int i=0;i<64;i++) basis[i]=0;
int rank=0;
for(int i=0;i<n;i++){
  unsigned long long x=squarefree_hash(a[i]);
  for(int b=63;b>=0;b--){
    if(((x>>b)&1ULL)==0ULL) continue;
    if(!basis[b]){ basis[b]=x; rank++; break; }
    x ^= basis[b];
  }
}
long long exp=(long long)n-rank;
long long r=1,a2=2%MOD;
while(exp){ if(exp&1) r=r*a2%MOD; a2=a2*a2%MOD; exp>>=1; }
r=(r-1+MOD)%MOD;
return r;
}

void print_ll(long long x) {
printf("%lld\n", x);
}

int main(void){ int n; static long long a[200005]; read_input(&n,a); long long ans=count_square_subseq(n,a); print_ll(ans); return 0; }
