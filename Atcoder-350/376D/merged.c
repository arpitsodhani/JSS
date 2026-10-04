#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int *M,int **U,int **V){ scanf("%d%d", N,M); *U=(int*)malloc((size_t)(*M)*sizeof(int)); *V=(int*)malloc((size_t)(*M)*sizeof(int)); for(int i=0;i<*M;i++) scanf("%d%d", &(*U)[i], &(*V)[i]); }

void build_adj(int N,int M,int *U,int *V,int *head,int *to,int *next){ for(int i=1;i<=N;i++) head[i]=-1; int ec=0; for(int i=0;i<M;i++){ int a=U[i], b=V[i]; to[ec]=b; next[ec]=head[a]; head[a]=ec++; } }

int bfs(int N,int s,int t,int *head,int *to,int *next){ int *q=(int*)malloc((size_t)(N+1)*sizeof(int)); int *dist=(int*)malloc((size_t)(N+1)*sizeof(int)); for(int i=1;i<=N;i++) dist[i]=-1; int h=0,tt=0; q[tt++]=s; dist[s]=0; while(h<tt){ int v=q[h++]; if(v==t) break; for(int e=head[v]; e!=-1; e=next[e]){ int u=to[e]; if(dist[u]==-1){ dist[u]=dist[v]+1; q[tt++]=u; } } } int ans=dist[t]; free(q); free(dist); return ans; }

int shortest_cycle(int N,int M,int *U,int *V){ int *head=(int*)malloc((size_t)(N+1)*sizeof(int)); int *to=(int*)malloc((size_t)M*sizeof(int)); int *next=(int*)malloc((size_t)M*sizeof(int)); build_adj(N,M,U,V,head,to,next); int best=1e9; for(int i=0;i<M;i++){ int u=U[i], v=V[i]; int d=bfs(N,v,u,head,to,next); if(d!=-1 && d+1<best) best=d+1; } free(head); free(to); free(next); if(best==1e9) return -1; return best; }

void print_answer(int ans){ printf("%d\n", ans); }

int main(void){ int N,M; int *U=NULL,*V=NULL; read_input(&N,&M,&U,&V); int ans=shortest_cycle(N,M,U,V); print_answer(ans); free(U); free(V); return 0; }
