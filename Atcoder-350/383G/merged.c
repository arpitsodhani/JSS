#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int *K,long long **A){ scanf("%d%d", N,K); *A=(long long*)malloc((size_t)(*N)*sizeof(long long)); for(int i=0;i<*N;i++) scanf("%lld", &(*A)[i]); }

void max_sums(int N,int K,long long *A,long long *out){
    int T = N / K;
    long long *pref=(long long*)malloc((size_t)(N+1)*sizeof(long long));
    pref[0]=0; for(int i=0;i<N;i++) pref[i+1]=pref[i]+A[i];
    long long *seg=(long long*)malloc((size_t)N*sizeof(long long));
    for(int i=0;i+K<=N;i++) seg[i]=pref[i+K]-pref[i];
    long long *dp=(long long*)malloc((size_t)(N+1)*sizeof(long long));
    for(int t=1;t<=T;t++){
        for(int i=0;i<=N;i++) dp[i]=0;
        for(int i=K;i<=N;i++){
            long long take = seg[i-K];
            long long val = dp[i-K] + take;
            dp[i] = dp[i-1] > val ? dp[i-1] : val;
        }
        out[t]=dp[N];
    }
    free(pref); free(seg); free(dp);
}

void print_answer(int N,int K,long long *out){ int T=N/K; for(int i=1;i<=T;i++) printf("%lld\n", out[i]); }

int main(void){ int N,K; long long *A=NULL; read_input(&N,&K,&A); int T=N/K; long long *out=(long long*)malloc((size_t)(T+1)*sizeof(long long)); max_sums(N,K,A,out); print_answer(N,K,out); free(A); free(out); return 0; }
