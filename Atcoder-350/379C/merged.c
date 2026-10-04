#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int *M,int **X,long long **A){ scanf("%d%d", N,M); *X=(int*)malloc((size_t)(*M)*sizeof(int)); *A=(long long*)malloc((size_t)(*M)*sizeof(long long)); for(int i=0;i<*M;i++) scanf("%d%lld", &(*X)[i], &(*A)[i]); }

void build_cells(int N,int M,int *X,long long *A,long long *cells){ for(int i=0;i<N;i++) cells[i]=0; for(int i=0;i<M;i++) cells[X[i]-1]=A[i]; }

long long min_moves(int N,long long *cells){ long long cur=0,ops=0; for(int i=0;i<N;i++){ cur+=cells[i]; if(cur==0) return -1; cur--; ops+=cur; } if(cur!=0) return -1; return ops; }

void print_answer(long long ans){ printf("%lld\n", ans); }

int main(void){ int N,M; int *X=NULL; long long *A=NULL; read_input(&N,&M,&X,&A); long long *cells=(long long*)malloc((size_t)N*sizeof(long long)); build_cells(N,M,X,A,cells); long long ans=min_moves(N,cells); print_answer(ans); free(X); free(A); free(cells); return 0; }
