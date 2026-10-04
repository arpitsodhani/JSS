#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lca(int u, int v, const int *up, const int *depth, int LOG, int stride) {
int lca(int u,int v,const int*up,const int*depth,int LOG,int stride){ if(depth[u]<depth[v]){ int t=u;u=v;v=t; } int diff=depth[u]-depth[v]; for(int k=0;k<LOG;k++) if(diff&(1<<k)) u=up[(size_t)k*stride+u]; if(u==v) return u; for(int k=LOG-1;k>=0;k--){ int pu=up[(size_t)k*stride+u], pv=up[(size_t)k*stride+v]; if(pu!=pv){ u=pu; v=pv; } } return up[u]; }
}

void solve(void){
  int N; scanf("%d", &N);
  int m=N-1;
  int *head=(int*)malloc((size_t)(N+1)*sizeof(int));
  int *to=(int*)malloc((size_t)(2*m)*sizeof(int));
  int *nx=(int*)malloc((size_t)(2*m)*sizeof(int));
  long long *w=(long long*)malloc((size_t)(2*m)*sizeof(long long));
  for(int i=1;i<=N;i++) head[i]=-1;
  int ec=0;
  for(int i=0;i<m;i++){ int a,b; long long c; scanf("%d %d %lld", &a, &b, &c);
    to[ec]=b; w[ec]=c; nx[ec]=head[a]; head[a]=ec++;
    to[ec]=a; w[ec]=c; nx[ec]=head[b]; head[b]=ec++;
  }
  int LOG=0; while((1<<LOG)<=N) LOG++;
  int stride=N+1;
  int *up=(int*)malloc((size_t)LOG*stride*sizeof(int));
  int *depth=(int*)malloc((size_t)stride*sizeof(int));
  long long *dist=(long long*)malloc((size_t)stride*sizeof(long long));
  int *q=(int*)malloc((size_t)(N+5)*sizeof(int));
  int qh=0,qt=0;
  q[qt++]=1; up[1]=1; depth[1]=0; dist[1]=0;
  while(qh<qt){ int v=q[qh++]; for(int e=head[v];e!=-1;e=nx[e]){ int u=to[e]; if(u==up[v]) continue; up[u]=v; depth[u]=depth[v]+1; dist[u]=dist[v]+w[e]; q[qt++]=u; } }
  for(int k=1;k<LOG;k++) for(int v=1;v<=N;v++) up[(size_t)k*stride+v]=up[(size_t)(k-1)*stride + up[(size_t)(k-1)*stride+v]];
  int Q; scanf("%d", &Q);
  for(int i=0;i<Q;i++){ int u,v; scanf("%d %d", &u, &v); int a=lca(u,v,up,depth,LOG,stride); long long ans=dist[u]+dist[v]-2LL*dist[a]; printf("%lld\n", ans); }
  free(head); free(to); free(nx); free(w); free(up); free(depth); free(dist); free(q);
}

int main(void){ solve(); return 0; }
