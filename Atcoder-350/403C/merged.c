#include <stdio.h>
#include <stdlib.h>

void read_input(int *n, int *W, int *w, long long *v) {
scanf("%d %d", n, W); for(int i=0;i<*n;i++) scanf("%d %lld", &w[i], &v[i]);
}

long long knap(int n, int W, const int *w, const long long *v) {
long long *dp=(long long*)malloc((size_t)(W+1)*sizeof(long long));
for(int i=0;i<=W;i++) dp[i]=0;
for(int i=0;i<n;i++){
  int wi=w[i]; long long vi=v[i];
  for(int cap=W;cap>=wi;cap--){
    long long cand=dp[cap-wi]+vi;
    if(cand>dp[cap]) dp[cap]=cand;
  }
}
long long ans=0; for(int cap=0;cap<=W;cap++) if(dp[cap]>ans) ans=dp[cap];
free(dp);
return ans;
}

void print_ll(long long x) {
printf("%lld\n", x);
}

int main(void){ int n,W; static int w[105]; static long long v[105]; read_input(&n,&W,w,v); long long ans=knap(n,W,w,v); print_ll(ans); return 0; }
