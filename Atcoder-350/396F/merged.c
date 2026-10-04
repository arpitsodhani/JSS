#include <stdio.h>
#include <stdlib.h>

void read_input(int *n, int *m, int *a) {
scanf("%d %d", n, m); for(int i=0;i<*n;i++) scanf("%d", &a[i]);
}

void bit_add(long long *bit, int n, int idx, long long v) {
for(int i=idx;i<=n;i+=i&-i) bit[i]+=v;
}

long long bit_sum(const long long *bit, int idx) {
long long s=0; for(int i=idx;i>0;i-=i&-i) s+=bit[i]; return s;
}

long long inversions0(int n, int m, const int *a) {
long long *bit=(long long*)calloc((size_t)(m+2),sizeof(long long));
long long inv=0;
for(int i=0;i<n;i++){
  int x=a[i]+1;
  long long le=bit_sum(bit,x);
  inv += (long long)i - le;
  bit_add(bit,m+1,x,1);
}
free(bit);
return inv;
}

void all_shifts(int n, int m, const int *a) {
long long inv=inversions0(n,m,a);
int *cnt=(int*)calloc((size_t)m,sizeof(int));
long long *sumpos=(long long*)calloc((size_t)m,sizeof(long long));
for(int i=0;i<n;i++){ int x=a[i]%m; cnt[x]++; sumpos[x]+=i; }
for(int k=0;k<m;k++){
  printf("%lld\n", inv);
  int r=(m-1-k)%m;
  long long c=cnt[r];
  long long sp=sumpos[r];
  long long delta = 2LL*sp - c*(long long)n + c;
  inv += delta;
}
free(cnt); free(sumpos);
}

int main(void){ int n,m; static int a[200005]; read_input(&n,&m,a); all_shifts(n,m,a); return 0; }
