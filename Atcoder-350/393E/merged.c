#include <stdio.h>
#include <stdlib.h>

void read_input(int *n,int *k,long long *A) {
scanf("%d%d", n,k); for(int i=0;i<*n;i++) scanf("%lld", &A[i]);
}

int list_divs(long long x,long long *divs) {
int cnt=0; for(long long d=1; d*d<=x; d++) if(x%d==0){ divs[cnt++]=d; if(d*d!=x) divs[cnt++]=x/d; }
return cnt;
}

void max_gcds(int n,int k,long long *A,long long *out) {
int maxd=0; for(int i=0;i<n;i++) if(A[i]>maxd) maxd=(int)A[i];
long long *divs=(long long*)malloc((size_t)100000*sizeof(long long));
int *cnt=(int*)calloc((size_t)(maxd+1),sizeof(int));
for(int i=0;i<n;i++){
  int c=list_divs(A[i],divs);
  for(int j=0;j<c;j++) if(divs[j]<=maxd) cnt[divs[j]]++;
}
for(int i=0;i<n;i++){
  long long best=1; int c=list_divs(A[i],divs);
  for(int j=0;j<c;j++) if(cnt[divs[j]]>=k && divs[j]>best) best=divs[j];
  out[i]=best;
}
free(cnt); free(divs);
}

void print_all(int n,long long *out) {
for(int i=0;i<n;i++) printf("%lld\n", out[i]);
}

int main(void){ int n,k; static long long A[200005],out[200005]; read_input(&n,&k,A); max_gcds(n,k,A,out); print_all(n,out); return 0; }
