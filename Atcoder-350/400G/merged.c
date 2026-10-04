#include <stdio.h>
#include <stdlib.h>

int better_pair(long long aval, int acnt, long long bval, int bcnt) {
if(aval!=bval) return aval>bval; return acnt>bcnt;
}

void solve_c(long long c, int n, long long (*x)[3], long long *out_val, int *out_cnt) {
const long long NEG = -(long long)4000000000000000000LL;
long long dpv[8]; int dpc[8];
for(int m=0;m<8;m++){ dpv[m]=NEG; dpc[m]=0; }
dpv[0]=0; dpc[0]=0;
for(int i=0;i<n;i++){
  long long ndpv[8]; int ndpc[8];
  for(int m=0;m<8;m++){ ndpv[m]=dpv[m]; ndpc[m]=dpc[m]; }
  for(int mask=0;mask<8;mask++){
    if(dpv[mask] <= NEG/2) continue;
    for(int d=0;d<3;d++){
      long long v = dpv[mask] + 2LL*x[i][d] - c;
      int cnt = dpc[mask] + 1;
      int nmask = mask ^ (1<<d);
      if(better_pair(v,cnt,ndpv[nmask],ndpc[nmask])){ ndpv[nmask]=v; ndpc[nmask]=cnt; }
    }
  }
  for(int m=0;m<8;m++){ dpv[m]=ndpv[m]; dpc[m]=ndpc[m]; }
}
*out_val = dpv[0];
*out_cnt = dpc[0];
}

long long solve_one_case(int n, int k, long long (*x)[3]) {
long long L=0, R=(1LL<<31);
while(L+1<R){
  long long M=(L+R)/2;
  long long v; int cnt;
  solve_c(M,n,x,&v,&cnt);
  if(cnt >= 2*k) L=M; else R=M;
}
long long v; int cnt;
solve_c(L,n,x,&v,&cnt);
long long ans = (v + 2LL*k*L)/2LL;
return ans;
}

int main(void){ int T; if(scanf("%d", &T)!=1) return 0; while(T--){ int n,k; scanf("%d %d", &n, &k); long long (*x)[3]=(long long(*)[3])malloc((size_t)n*sizeof(long long[3])); for(int i=0;i<n;i++) scanf("%lld %lld %lld", &x[i][0], &x[i][1], &x[i][2]); long long ans=solve_one_case(n,k,x); printf("%lld\n", ans); free(x); } return 0; }
