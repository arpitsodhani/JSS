#include <stdio.h>
#include <stdlib.h>

void read_grid(int *h, int *w, int *cnt, int *mask) {
scanf("%d %d", h, w);
int W=*w;
for(int i=0;i<(1<<W);i++) cnt[i]=0;
for(int i=0;i<*h;i++){
  char s[25]; scanf("%s", s);
  int m=0;
  for(int j=0;j<W;j++) if(s[j]=='1') m |= (1<<j);
  cnt[m]++;
}
*mask=0;
}

void fwht(long long *a, int n, int inv) {
for(int len=1; 2*len<=n; len<<=1){
  for(int i=0;i<n;i+=2*len){
    for(int j=0;j<len;j++){
      long long u=a[i+j], v=a[i+j+len];
      a[i+j]=u+v;
      a[i+j+len]=u-v;
    }
  }
}
if(inv){
  for(int i=0;i<n;i++) a[i]/=n;
}
}

long long min_ones(int h, int w, const int *cnt) {
int N=1<<w;
long long *F=(long long*)malloc((size_t)N*sizeof(long long));
for(int i=0;i<N;i++) F[i]=cnt[i];
fwht(F,N,0);
long long *sum=(long long*)calloc((size_t)N,sizeof(long long));
for(int t=0;t<=w;t++){
  long long *H=(long long*)malloc((size_t)N*sizeof(long long));
  for(int i=0;i<N;i++) H[i]=(__builtin_popcount((unsigned)i)==t)?1:0;
  fwht(H,N,0);
  long long *G=(long long*)malloc((size_t)N*sizeof(long long));
  for(int i=0;i<N;i++) G[i]=F[i]*H[i];
  fwht(G,N,1);
  long long wcost = (long long)((t < w-t)?t:(w-t));
  for(int mask=0;mask<N;mask++) sum[mask] += G[mask]*wcost;
  free(H); free(G);
}
long long best=sum[0];
for(int mask=1;mask<N;mask++) if(sum[mask]<best) best=sum[mask];
free(F); free(sum);
return best;
}

int main(void){ int h,w,mask; int *cnt=(int*)malloc((size_t)(1<<18)*sizeof(int)); read_grid(&h,&w,cnt,&mask); long long ans=min_ones(h,w,cnt); printf("%lld\n", ans); free(cnt); return 0; }
