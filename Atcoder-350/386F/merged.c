#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_input(int *N,int *K,char *s) {
scanf("%d%d", N,K); scanf("%s", s);
}

int can_make(int N,int K,const char *s,const char *t) {
int n=strlen(s), m=strlen(t); if(n-m> K || m-n> K) return 0;
int W=2*K+1; int *dp=(int*)malloc((size_t)(W+2)*sizeof(int)); int *ndp=(int*)malloc((size_t)(W+2)*sizeof(int));
for(int i=0;i<=W;i++) dp[i]=1e9; dp[K]=0;
for(int i=0;i<=n;i++){
  for(int j=0;j<=W;j++) ndp[j]=1e9;
  int jmin=i-K; if(jmin<0) jmin=0; int jmax=i+K; if(jmax>m) jmax=m;
  for(int j=jmin;j<=jmax;j++){
    int d=j-i+K; if(dp[d]>=1e9) continue;
    if(i<n && j<m){ int cost= (s[i]==t[j])?0:1; if(dp[d]+cost<ndp[d]) ndp[d]=dp[d]+cost; }
    if(i<n && d+1<=W) if(dp[d]+1<ndp[d+1]) ndp[d+1]=dp[d]+1; /* delete */
    if(j<m && d-1>=0) if(dp[d]+1<ndp[d-1]) ndp[d-1]=dp[d]+1; /* insert */
  }
  int *tmp=dp; dp=ndp; ndp=tmp;
}
int ok= dp[m-n+K] <= K; free(dp); free(ndp); return ok;
}

void print_yesno(int x) {
printf("%s\n", x?"Yes":"No");
}

int main(void){ int N,K; static char s[600005],t[600005]; read_input(&N,&K,s); scanf("%s", t); int ok=can_make(N,K,s,t); print_yesno(ok); return 0;}
