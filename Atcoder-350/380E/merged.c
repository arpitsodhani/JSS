#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int **A){ scanf("%d", N); *A=(int*)malloc((size_t)(*N)*sizeof(int)); for(int i=0;i<*N;i++) scanf("%d", &(*A)[i]); }

int init_max(int *A){ return A[0]; }

int update_max(int cur,int val){ return val>cur?val:cur; }

int finalize_max(int mx){ return mx; }

int find_max(int N,int *A){
    int mx=init_max(A);
    for(int i=1;i<N;i++) mx=update_max(mx,A[i]);
    return finalize_max(mx);
}

void print_answer(int ans){ printf("%d\n", ans); }

int main(void){ int N; int *A=NULL; read_input(&N,&A); int ans=find_max(N,A); print_answer(ans); free(A); return 0; }
