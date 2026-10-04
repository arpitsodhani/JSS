#include <stdio.h>

void read_input(int *n, int *k, int *a) {
scanf("%d %d", n, k); for(int i=0;i<*n;i++) scanf("%d", &a[i]);
}

void build_binom(int k, long long *c) {
for(int i=0;i<=k;i++) c[i]=0;
c[0]=1;
for(int i=1;i<=k;i++){
  for(int j=i;j>=1;j--) c[j]=(c[j]+c[j-1])%998244353LL;
}
}

long long sum_pows(int n, int k, const int *a) {
const long long MOD=998244353LL;
long long *C=(long long*)malloc((size_t)(k+1)*sizeof(long long));
build_binom(k,C);
long long S[11];
for(int i=0;i<=k;i++) S[i]=0;
S[0]=1;
long long pref=0;
long long ans=0;
for(int r=1;r<=n;r++){
  pref += a[r-1]; pref%=MOD;
  long long powx[11]; powx[0]=1;
  for(int i=1;i<=k;i++) powx[i]=powx[i-1]*pref%MOD;
  long long add=0;
  for(int t=0;t<=k;t++){
    long long term = C[t] * powx[t] % MOD;
    int p=k-t;
    long long s=S[p];
    if(p%2==1) s=(MOD-s)%MOD;
    add = (add + term * s)%MOD;
  }
  ans = (ans + add)%MOD;
  long long powp[11]; powp[0]=1;
  for(int i=1;i<=k;i++) powp[i]=powp[i-1]*pref%MOD;
  for(int i=0;i<=k;i++) S[i]=(S[i]+powp[i])%MOD;
}
free(C);
return ans;
}

int main(void){ int n,k; static int a[200005]; read_input(&n,&k,a); long long ans=sum_pows(n,k,a); printf("%lld\n", ans); return 0; }
