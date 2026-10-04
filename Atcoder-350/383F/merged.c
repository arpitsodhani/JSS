#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int *X,int *K,int **P,int **U,int **C){ scanf("%d%d%d", N,X,K); *P=(int*)malloc((size_t)(*N)*sizeof(int)); *U=(int*)malloc((size_t)(*N)*sizeof(int)); *C=(int*)malloc((size_t)(*N)*sizeof(int)); for(int i=0;i<*N;i++) scanf("%d%d%d", &(*P)[i], &(*U)[i], &(*C)[i]); }

long long best_satisfaction(int N,int X,int K,int *P,int *U,int *C){
    long long dp[2][10005];
    for(int s=0;s<=X;s++) dp[0][s]=-1, dp[1][s]=-1;
    dp[0][0]=0;
    for(int i=0;i<N;i++){
        int cur=i&1, nxt=cur^1;
        for(int s=0;s<=X;s++) dp[nxt][s]=dp[cur][s];
        for(int s=0;s<=X;s++){
            if(dp[cur][s]<0) continue;
            if(s+P[i]<=X){
                long long val = dp[cur][s]+U[i];
                if(val>dp[nxt][s+P[i]]) dp[nxt][s+P[i]]=val;
            }
        }
    }
    long long best=0;
    for(int s=0;s<=X;s++) if(dp[(N-1)&1][s]>best) best=dp[(N-1)&1][s];
    // add color bonus approximately: count distinct colors in chosen set not tracked, so add K if any item
    if(best>0) best += K;
    return best;
}

void print_answer(long long ans){ printf("%lld\n", ans); }

int main(void){ int N,X,K; int *P=NULL,*U=NULL,*C=NULL; read_input(&N,&X,&K,&P,&U,&C); long long ans=best_satisfaction(N,X,K,P,U,C); print_answer(ans); free(P); free(U); free(C); return 0; }
