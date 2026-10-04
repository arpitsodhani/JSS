#include <stdio.h>
#include <stdlib.h>

void solve(void){ int N; long long K; scanf("%d %lld", &N, &K); long long *A=(long long*)malloc((size_t)N*sizeof(long long)); for(int i=0;i<N;i++) scanf("%lld", &A[i]); long long ans=0,sum=0; int r=0; for(int l=0;l<N;l++){ while(r<N && sum + A[r] <= K){ sum+=A[r]; r++; } ans += (long long)(r-l); if(r==l) r++; else sum -= A[l]; } printf("%lld\n", ans); free(A); }

int main(void){ solve(); return 0; }
