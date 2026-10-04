#include <stdio.h>
#include <stdlib.h>

void read_input(int *n, int *m, long long *b, long long *w) {
scanf("%d %d", n, m); for(int i=0;i<*n;i++) scanf("%lld", &b[i]); for(int j=0;j<*m;j++) scanf("%lld", &w[j]);
}

int cmp_ll_desc(const void *p, const void *q) {
long long a=*(const long long*)p, b=*(const long long*)q; if(a>b) return -1; if(a<b) return 1; return 0;
}

long long max_sum(int n, int m, long long *b, long long *w) {
qsort(b,(size_t)n,sizeof(long long),cmp_ll_desc);
qsort(w,(size_t)m,sizeof(long long),cmp_ll_desc);
long long *pb=(long long*)malloc((size_t)(n+1)*sizeof(long long));
long long *pw=(long long*)malloc((size_t)(m+1)*sizeof(long long));
pb[0]=0; for(int i=0;i<n;i++) pb[i+1]=pb[i]+b[i];
pw[0]=0; for(int j=0;j<m;j++) pw[j+1]=pw[j]+w[j];
for(int i=0;i<=n;i++) if(pb[i]<0) pb[i]=-(1LL<<60);
long long bestw=0; long long ans=0;
int jmax=0;
for(int i=0;i<=n;i++){
  int lim=i; if(lim>m) lim=m;
  while(jmax<lim){ jmax++; if(pw[jmax]>bestw) bestw=pw[jmax]; }
  long long cand=pb[i] + bestw;
  if(cand>ans) ans=cand;
}
free(pb); free(pw);
return ans;
}

int main(void){ int n,m; static long long b[200005], w[200005]; read_input(&n,&m,b,w); long long ans=max_sum(n,m,b,w); printf("%lld\n", ans); return 0; }
