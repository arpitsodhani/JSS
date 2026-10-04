#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int *K,long long **A,long long **B){ scanf("%d%d", N,K); *A=(long long*)malloc((size_t)(*N)*sizeof(long long)); *B=(long long*)malloc((size_t)(*N)*sizeof(long long)); for(int i=0;i<*N;i++) scanf("%lld%lld", &(*A)[i], &(*B)[i]); }

void sort_pairs(int N,long long *A,long long *B){ for(int i=0;i<N;i++) for(int j=i+1;j<N;j++) if(A[j]<A[i]){ long long ta=A[i]; A[i]=A[j]; A[j]=ta; long long tb=B[i]; B[i]=B[j]; B[j]=tb; } }

long long best_value(int N,int K,long long *A,long long *B){ long long sum=0,ans=0; for(int i=0;i<N;i++){ sum+=B[i]; if(i>=K-1){ if(sum*A[i]>ans) ans=sum*A[i]; } } return ans; }

void print_answer(long long ans){ printf("%lld\n", ans); }

int main(void){ int N,K; long long *A=NULL,*B=NULL; read_input(&N,&K,&A,&B); sort_pairs(N,A,B); long long ans=best_value(N,K,A,B); print_answer(ans); free(A); free(B); return 0; }
