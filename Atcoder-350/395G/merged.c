#include <stdio.h>
#include <stdlib.h>

void read_input(int *n, int *k, int *q, long long *c) {
scanf("%d %d", n, k);
for(int i=0;i<*n;i++) for(int j=0;j<*n;j++){ long long x; scanf("%lld", &x); c[i*(*n)+j]=x; }
scanf("%d", q);
}

void floyd(int n, long long *d) {
for(int k=0;k<n;k++){
  for(int i=0;i<n;i++){
    long long dik=d[i*n+k];
    for(int j=0;j<n;j++){
      long long v=dik + d[k*n+j];
      if(v<d[i*n+j]) d[i*n+j]=v;
    }
  }
}
}

void steiner_base(int n, int k, const long long *d, long long *best_to) {
int T=k;
int S=1<<T;
long long INF=4000000000000000000LL;
long long *dp=(long long*)malloc((size_t)S*(size_t)n*sizeof(long long));
for(int m=0;m<S*n;m++) dp[m]=INF;
for(int i=0;i<T;i++) dp[(1<<i)*n + i]=0;
for(int mask=1;mask<S;mask++){
  for(int sub=(mask-1)&mask; sub; sub=(sub-1)&mask){
    int other=mask^sub;
    for(int v=0;v<n;v++){
      long long a=dp[sub*n+v], b=dp[other*n+v];
      long long c=a+b;
      if(c<dp[mask*n+v]) dp[mask*n+v]=c;
    }
  }
  // relax by shortest paths
  int upd=1;
  while(upd){
    upd=0;
    for(int v=0;v<n;v++){
      long long dv=dp[mask*n+v];
      for(int u=0;u<n;u++){
        long long nd=d[v*n+u]+dv;
        if(nd<dp[mask*n+u]){ dp[mask*n+u]=nd; upd=1; }
      }
    }
  }
}
int full=S-1;
for(int v=0;v<n;v++) best_to[v]=dp[full*n+v];
free(dp);
}

long long answer_query(int n, int k, const long long *d, const long long *best_to, int s, int t) {
long long ans=4000000000000000000LL;
for(int m=0;m<n;m++){
  long long cand=best_to[m] + d[m*n+s] + d[m*n+t];
  if(cand<ans) ans=cand;
}
return ans;
}

int main(void){ int n,k,q; long long *c=(long long*)malloc((size_t)80*(size_t)80*sizeof(long long));
read_input(&n,&k,&q,c);
floyd(n,c);
long long *best_to=(long long*)malloc((size_t)n*sizeof(long long));
steiner_base(n,k,c,best_to);
for(int i=0;i<q;i++){
  int s,t; scanf("%d %d", &s,&t); s--; t--;
  long long ans=answer_query(n,k,c,best_to,s,t);
  printf("%lld\n", ans);
}
free(best_to); free(c);
return 0; }
