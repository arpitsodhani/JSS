#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int **U,int **V){ scanf("%d", N); *U=(int*)malloc((size_t)(*N-1)*sizeof(int)); *V=(int*)malloc((size_t)(*N-1)*sizeof(int)); for(int i=0;i<*N-1;i++) scanf("%d%d", &(*U)[i], &(*V)[i]); }

void build_adj(int N,int *U,int *V,int *head,int *to,int *next){ for(int i=1;i<=N;i++) head[i]=-1; int ec=0; for(int i=0;i<N-1;i++){ int a=U[i], b=V[i]; to[ec]=b; next[ec]=head[a]; head[a]=ec++; to[ec]=a; next[ec]=head[b]; head[b]=ec++; } }

int find_path(int N,int s,int t,int *head,int *to,int *next,int *par){
    int *q=(int*)malloc((size_t)(N+1)*sizeof(int));
    for(int i=1;i<=N;i++) par[i]=-1;
    int h=0,tt=0; q[tt++]=s; par[s]=s;
    while(h<tt){
        int v=q[h++]; if(v==t) break;
        for(int e=head[v]; e!=-1; e=next[e]){
            int u=to[e];
            if(par[u]==-1){ par[u]=v; q[tt++]=u; }
        }
    }
    free(q);
    return par[t]!=-1;
}

long long count_cycles(int N,int *U,int *V){
    int *head=(int*)malloc((size_t)(N+1)*sizeof(int));
    int *to=(int*)malloc((size_t)2*(N-1)*sizeof(int));
    int *next=(int*)malloc((size_t)2*(N-1)*sizeof(int));
    build_adj(N,U,V,head,to,next);
    int *deg=(int*)malloc((size_t)(N+1)*sizeof(int));
    for(int i=1;i<=N;i++) deg[i]=0;
    for(int i=0;i<N-1;i++){ deg[U[i]]++; deg[V[i]]++; }
    long long ans=0;
    int *par=(int*)malloc((size_t)(N+1)*sizeof(int));
    for(int u=1; u<=N; u++){
        for(int v=u+1; v<=N; v++){
            if(!find_path(N,u,v,head,to,next,par)) continue;
            int ok=1;
            int x=v;
            while(x!=u){
                int p=par[x];
                if(x!=u && x!=v){ if(deg[x]!=3) ok=0; }
                x=p;
            }
            if(deg[u]!=2 || deg[v]!=2) ok=0;
            if(ok) ans++;
        }
    }
    free(head); free(to); free(next); free(deg); free(par);
    return ans;
}

void print_answer(long long ans){ printf("%lld\n", ans); }

int main(void){ int N; int *U=NULL,*V=NULL; read_input(&N,&U,&V); long long ans=count_cycles(N,U,V); print_answer(ans); free(U); free(V); return 0; }
