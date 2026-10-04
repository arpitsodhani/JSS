#include <stdio.h>
#include <stdlib.h>

void read_graph(int *n, int *m, int *u, int *v, unsigned long long *w) {
scanf("%d %d", n, m); for(int i=0;i<*m;i++){ scanf("%d %d %llu", &u[i], &v[i], &w[i]); u[i]--; v[i]--; }
}

void dfs(int n, int cur, int target, int *vis, int *head, int *to, int *nx, unsigned long long *ew, unsigned long long acc, unsigned long long *best) {
if(cur==target){ if(acc<*best) *best=acc; return; }
for(int e=head[cur]; e!=-1; e=nx[e]){
  int y=to[e];
  if(vis[y]) continue;
  vis[y]=1;
  dfs(n,y,target,vis,head,to,nx,ew,acc^ew[e],best);
  vis[y]=0;
}
}

unsigned long long min_xor_path(int n, int m, const int *u, const int *v, const unsigned long long *w) {
int *head=(int*)malloc((size_t)n*sizeof(int));
int *to=(int*)malloc((size_t)(2*m)*sizeof(int));
int *nx=(int*)malloc((size_t)(2*m)*sizeof(int));
unsigned long long *ew=(unsigned long long*)malloc((size_t)(2*m)*sizeof(unsigned long long));
for(int i=0;i<n;i++) head[i]=-1;
int ec=0;
for(int i=0;i<m;i++){
  int a=u[i], b=v[i];
  to[ec]=b; ew[ec]=w[i]; nx[ec]=head[a]; head[a]=ec++;
  to[ec]=a; ew[ec]=w[i]; nx[ec]=head[b]; head[b]=ec++;
}
int vis[12]={0}; vis[0]=1;
unsigned long long best=~0ULL;
dfs(n,0,n-1,vis,head,to,nx,ew,0ULL,&best);
free(head); free(to); free(nx); free(ew);
return best;
}

int main(void){ int n,m; static int u[60], v[60]; static unsigned long long w[60]; read_graph(&n,&m,u,v,w); unsigned long long ans=min_xor_path(n,m,u,v,w); printf("%llu\n", ans); return 0; }
