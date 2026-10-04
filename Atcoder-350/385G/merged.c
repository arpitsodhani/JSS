#include <stdio.h>

void read_input(int *N,int *K) {
scanf("%d%d", N,K);
}

long long solve(int N,int K) {
const long long MOD=998244353LL;
static long long dp[405][405][405];
dp[1][1][1]=1;
for(int n=2;n<=N;n++){
  for(int l=1;l<=n;l++) for(int r=1;r<=n;r++){
    long long v=0;
    if(l>1) v=(v+dp[n-1][l-1][r])%MOD;
    if(r>1) v=(v+dp[n-1][l][r-1])%MOD;
    v=(v + dp[n-1][l][r]*(long long)(n-2))%MOD;
    dp[n][l][r]=v;
  }
}
long long ans=0;
for(int l=1;l<=N;l++) for(int r=1;r<=N;r++) if(l-r==K) ans=(ans+dp[N][l][r])%MOD;
if(ans<0) ans+=MOD; return ans;
}

void print_ll(long long x) {
printf("%lld\n", x);
}

int main(void){ int N,K; read_input(&N,&K); long long ans=solve(N,K); print_ll(ans); return 0;}
