#include <stdio.h>
#include <stdlib.h>

void read_input(int *n, long long *k, long long *A, long long *B, long long *C) {
scanf("%d%lld", n, k);
for(int i=0;i<*n;i++) scanf("%lld", &A[i]);
for(int i=0;i<*n;i++) scanf("%lld", &B[i]);
for(int i=0;i<*n;i++) scanf("%lld", &C[i]);
}

long long kth_value(int n, long long k, long long *A, long long *B, long long *C) {
long long total=(long long)n*n*n;
long long *vals=(long long*)malloc((size_t)total*sizeof(long long));
long long idx=0;
for(int i=0;i<n;i++) for(int j=0;j<n;j++) for(int t=0;t<n;t++){
  vals[idx++]=A[i]*B[j]+B[j]*C[t]+C[t]*A[i];
}
for(long long i=0;i<total;i++) for(long long j=i+1;j<total;j++) if(vals[j]>vals[i]){ long long tmp=vals[i]; vals[i]=vals[j]; vals[j]=tmp; }
long long ans=vals[k-1]; free(vals); return ans;
}

void print_ll(long long x) {
printf("%lld\n", x);
}

int main(void){ int n; long long k; static long long A[205],B[205],C[205]; read_input(&n,&k,A,B,C); long long ans=kth_value(n,k,A,B,C); print_ll(ans); return 0; }
