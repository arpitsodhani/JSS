#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int *M,int **L,int **R){ scanf("%d%d", N,M); *L=(int*)malloc((size_t)(*N)*sizeof(int)); *R=(int*)malloc((size_t)(*N)*sizeof(int)); for(int i=0;i<*N;i++) scanf("%d%d", &(*L)[i], &(*R)[i]); }

long long count_pairs(int N,int M,int *L,int *R){ long long ans=0; for(int l=1;l<=M;l++){ for(int r=l;r<=M;r++){ int ok=1; for(int i=0;i<N;i++){ if(l<=L[i] && R[i]<=r){ ok=0; break; } } if(ok) ans++; } } return ans; }

void print_answer(long long ans){ printf("%lld\n", ans); }

int main(void){ int N,M; int *L=NULL,*R=NULL; read_input(&N,&M,&L,&R); long long ans=count_pairs(N,M,L,R); print_answer(ans); free(L); free(R); return 0; }
