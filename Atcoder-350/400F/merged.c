#include <stdio.h>
#include <stdlib.h>

void read_input(int *n, int *c, long long *x) {
scanf("%d", n);
for(int i=0;i<*n;i++){ scanf("%d", &c[i]); c[i]--; }
for(int i=0;i<*n;i++) scanf("%lld", &x[i]);
}

int* build_doubled_colors(int n, const int *c) {
int N2=2*n; int *cc=(int*)malloc((size_t)N2*sizeof(int)); for(int i=0;i<n;i++){ cc[i]=c[i]; cc[n+i]=c[i]; } return cc;
}

void init_tables(int N2, long long **dp, long long **ep, long long INF) {
for(int i=0;i<=N2;i++){ for(int j=0;j<=N2;j++){ dp[i][j]=INF; ep[i][j]=INF; } dp[i][i]=0; ep[i][i]=0; }
}

long long solve_case(int n, const int *c, const long long *x) {
const long long INF=1000000000000000010LL;
int N2=2*n;
int *cc=build_doubled_colors(n,c);
long long **dp=(long long**)malloc((size_t)(N2+1)*sizeof(long long*));
long long **ep=(long long**)malloc((size_t)(N2+1)*sizeof(long long*));
for(int i=0;i<=N2;i++){ dp[i]=(long long*)malloc((size_t)(N2+1)*sizeof(long long)); ep[i]=(long long*)malloc((size_t)(N2+1)*sizeof(long long)); }
init_tables(N2,dp,ep,INF);
for(int l=N2;l>=0;l--){
  for(int r=l+1;r<=N2;r++){
    for(int m=l+1;m<r;m++){
      long long v1=dp[l][m]+dp[m][r]; if(v1<dp[l][r]) dp[l][r]=v1;
      long long v2=ep[l][m]+dp[m][r]; if(v2<ep[l][r]) ep[l][r]=v2;
    }
    if(cc[l]==cc[r-1]){
      if(ep[l][r-1]<ep[l][r]) ep[l][r]=ep[l][r-1];
      long long cand=ep[l][r] + (long long)(r-l) + x[cc[l]];
      if(cand<dp[l][r]) dp[l][r]=cand;
    }
  }
}
long long ans=INF;
for(int i=0;i<n;i++) if(dp[i][n+i]<ans) ans=dp[i][n+i];
for(int i=0;i<=N2;i++){ free(dp[i]); free(ep[i]); }
free(dp); free(ep); free(cc);
return ans;
}

void print_ll(long long v) {
printf("%lld\n", v);
}

int main(void){ int n; static int c[2005]; static long long x[2005]; read_input(&n,c,x); long long ans=solve_case(n,c,x); print_ll(ans); return 0; }
