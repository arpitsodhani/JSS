#include <stdio.h>
#include <stdlib.h>

int cmp_interval(const void *a, const void *b) {
int cmp_interval(const void*a,const void*b){ const long long*x=(const long long*)a; const long long*y=(const long long*)b; if(x[1]<y[1]) return -1; if(x[1]>y[1]) return 1; if(x[0]<y[0]) return -1; if(x[0]>y[0]) return 1; return 0; }
}

void solve(void){ int N; scanf("%d", &N); long long (*iv)[2]=(long long(*)[2])malloc((size_t)N*sizeof(long long[2])); for(int i=0;i<N;i++) scanf("%lld %lld", &iv[i][0], &iv[i][1]); qsort(iv,N,sizeof(iv[0]),cmp_interval); long long last=-(1LL<<60); int ans=0; for(int i=0;i<N;i++){ if(last<iv[i][0]){ last=iv[i][1]; ans++; } } printf("%d\n", ans); free(iv); }

int main(void){ solve(); return 0; }
