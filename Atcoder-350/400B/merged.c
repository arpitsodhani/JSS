#include <stdio.h>

void read_nm(long long *n, long long *m) {
scanf("%lld %lld", n, m);
}

int sum_geom(long long n, long long m, long long *out) {
long long x=1;
long long cur=1;
for(long long i=1;i<=m;i++){
  if(cur>1000000000LL/n && n!=0) return 0;
  cur*=n;
  if(x>1000000000LL-cur) return 0;
  x+=cur;
}
*out=x;
return 1;
}

int main(void){ long long n,m; read_nm(&n,&m); long long x=0; if(sum_geom(n,m,&x)) printf("%lld\n", x); else puts("inf"); return 0; }
