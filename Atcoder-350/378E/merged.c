#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int *M,int **A){ scanf("%d%d", N,M); *A=(int*)malloc((size_t)(*N)*sizeof(int)); for(int i=0;i<*N;i++) scanf("%d", &(*A)[i]); }

void build_prefix(int N,int M,int *A,int *P){ P[0]=0; for(int i=0;i<N;i++) P[i+1]=(P[i]+A[i])%M; }

long long sum_mods(int N,int M,int *P){ long long ans=0; for(int l=0;l<N;l++){ for(int r=l;r<N;r++){ int val=P[r+1]-P[l]; if(val<0) val+=M; ans+=val; } } return ans; }

void print_answer(long long ans){ printf("%lld\n", ans); }

int main(void){ int N,M; int *A=NULL; read_input(&N,&M,&A); int *P=(int*)malloc((size_t)(N+1)*sizeof(int)); build_prefix(N,M,A,P); long long ans=sum_mods(N,M,P); print_answer(ans); free(A); free(P); return 0; }
