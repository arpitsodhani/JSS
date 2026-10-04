#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int *M,int *K,int **U,int **V,int **W,int **A,int **B){ scanf("%d%d%d", N,M,K); *U=(int*)malloc((size_t)(*M)*sizeof(int)); *V=(int*)malloc((size_t)(*M)*sizeof(int)); *W=(int*)malloc((size_t)(*M)*sizeof(int)); for(int i=0;i<*M;i++) scanf("%d%d%d", &(*U)[i], &(*V)[i], &(*W)[i]); *A=(int*)malloc((size_t)(*K)*sizeof(int)); *B=(int*)malloc((size_t)(*K)*sizeof(int)); for(int i=0;i<*K;i++) scanf("%d", &(*A)[i]); for(int i=0;i<*K;i++) scanf("%d", &(*B)[i]); }

long long solve_min_sum(int N,int M,int K,int *U,int *V,int *W,int *A,int *B) {
typedef struct Edge{ int to; int w; int next; } Edge;
int dsu_find(int *par,int x){ while(par[x]!=x) x=par[x]; return x; }
long long solve_min_sum(int N,int M,int K,int *U,int *V,int *W,int *A,int *B){
    // build MST by Kruskal (heuristic for minimax path)
    int *idx=(int*)malloc((size_t)M*sizeof(int));
    for(int i=0;i<M;i++) idx[i]=i;
    for(int i=0;i<M;i++) for(int j=i+1;j<M;j++) if(W[idx[j]]<W[idx[i]]){ int t=idx[i]; idx[i]=idx[j]; idx[j]=t; }
    int *par=(int*)malloc((size_t)(N+1)*sizeof(int));
    int *sz=(int*)malloc((size_t)(N+1)*sizeof(int));
    for(int i=1;i<=N;i++){ par[i]=i; sz[i]=1; }
    int *head=(int*)malloc((size_t)(N+1)*sizeof(int));
    for(int i=1;i<=N;i++) head[i]=-1;
    Edge *edges=(Edge*)malloc((size_t)2*M*sizeof(Edge));
    int ec=0;
    for(int ii=0; ii<M; ii++){
        int e=idx[ii];
        int a=dsu_find(par,U[e]), b=dsu_find(par,V[e]);
        if(a!=b){
            if(sz[a]<sz[b]){ int t=a; a=b; b=t; }
            par[b]=a; sz[a]+=sz[b];
            edges[ec]=(Edge){V[e], W[e], head[U[e]]}; head[U[e]]=ec++;
            edges[ec]=(Edge){U[e], W[e], head[V[e]]}; head[V[e]]=ec++;
        }
    }
    // simple pairing: sort A and B and pair in order
    for(int i=0;i<K;i++) for(int j=i+1;j<K;j++) if(A[j]<A[i]){ int t=A[i]; A[i]=A[j]; A[j]=t; }
    for(int i=0;i<K;i++) for(int j=i+1;j<K;j++) if(B[j]<B[i]){ int t=B[i]; B[i]=B[j]; B[j]=t; }
    // BFS for each pair to compute max edge on path (slow but ok)
    long long sum=0;
    int *q=(int*)malloc((size_t)(N+5)*sizeof(int));
    int *vis=(int*)malloc((size_t)(N+1)*sizeof(int));
    int *mx=(int*)malloc((size_t)(N+1)*sizeof(int));
    for(int i=0;i<K;i++){
        for(int v=1; v<=N; v++){ vis[v]=0; mx[v]=0; }
        int s=A[i], t=B[i];
        int headq=0, tail=0;
        q[tail++]=s; vis[s]=1; mx[s]=0;
        while(headq<tail){
            int v=q[headq++];
            if(v==t) break;
            for(int e=head[v]; e!=-1; e=edges[e].next){
                int u=edges[e].to;
                if(!vis[u]){
                    vis[u]=1;
                    mx[u]=mx[v] > edges[e].w ? mx[v] : edges[e].w;
                    q[tail++]=u;
                }
            }
        }
        sum += mx[t];
    }
    free(idx); free(par); free(sz); free(head); free(edges); free(q); free(vis); free(mx);
    return sum;
}
}

void print_answer(long long ans){ printf("%lld\n", ans); }

int main(void){ int N,M,K; int *U=NULL,*V=NULL,*W=NULL,*A=NULL,*B=NULL; read_input(&N,&M,&K,&U,&V,&W,&A,&B); long long ans=solve_min_sum(N,M,K,U,V,W,A,B); print_answer(ans); free(U); free(V); free(W); free(A); free(B); return 0; }
