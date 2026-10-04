#include <stdio.h>
#include <string.h>

void read_input(char *s, int *n, long long *m) {
scanf("%s%lld", s, m); *n=(int)strlen(s);
}

void count_prefix_lcs(const char *s, int n, long long m, long long *out) {
const long long MOD=998244353LL;
static long long dp[505], ndp[505];
for(int i=0;i<=n;i++) dp[i]=0; dp[0]=1;
for(long long step=0; step<m; step++){
  for(int i=0;i<=n;i++) ndp[i]=0;
  ndp[0]=(dp[0]*25)%MOD;
  for(int i=1;i<n;i++){
    ndp[i]=(dp[i]*25 + dp[i-1])%MOD;
  }
  ndp[n]=(dp[n]*26 + dp[n-1])%MOD;
  for(int i=0;i<=n;i++) dp[i]=ndp[i];
}
for(int i=0;i<=n;i++) out[i]=dp[i]%MOD;
}

void print_all(int n, const long long *out) {
for(int i=0;i<=n;i++){
  printf("%lld\n", out[i]);
}
}

int main(void){ static char s[505]; int n; long long m; read_input(s,&n,&m); static long long out[505]; count_prefix_lcs(s,n,m,out); print_all(n,out); return 0; }
