#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int *M,int **U,int **V){ scanf("%d%d", N,M); *U=(int*)malloc((size_t)(*M)*sizeof(int)); *V=(int*)malloc((size_t)(*M)*sizeof(int)); for(int i=0;i<*M;i++) scanf("%d%d", &(*U)[i], &(*V)[i]); }

void build_adj(int N,int M,int *U,int *V,int *head,int *to,int *next){ for(int i=1;i<=N;i++) head[i]=-1; int ec=0; for(int i=0;i<M;i++){ int a=U[i], b=V[i]; to[ec]=b; next[ec]=head[a]; head[a]=ec++; to[ec]=a; next[ec]=head[b]; head[b]=ec++; } }

long long count_pairs(int N,int *head,int *to,int *next){ long long ans=0; for(int u=1;u<=N;u++){ for(int e=head[u]; e!=-1; e=next[e]){ int v=to[e]; if(v>u) ans++; } } return ans; }

void print_answer(long long ans){ printf("%lld\n", ans); }

int main(void){ int N,M; int *U=NULL,*V=NULL; read_input(&N,&M,&U,&V); int *head=(int*)malloc((size_t)(N+1)*sizeof(int)); int *to=(int*)malloc((size_t)2*M*sizeof(int)); int *next=(int*)malloc((size_t)2*M*sizeof(int)); build_adj(N,M,U,V,head,to,next); long long ans=count_pairs(N,head,to,next); print_answer(ans); free(U); free(V); free(head); free(to); free(next); return 0; }
