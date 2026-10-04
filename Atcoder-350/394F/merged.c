#include <stdio.h>
#include <stdlib.h>

void read_tree(int *n, int *u, int *v) {
scanf("%d", n); for(int i=0;i<*n-1;i++){ scanf("%d %d", &u[i], &v[i]); u[i]--; v[i]--; }
}

void add_edge(int a, int b, int *head, int *to, int *nx, int *ec) {
to[*ec]=b; nx[*ec]=head[a]; head[a]=(*ec)++;
}

void dfs1(int u, int p, const int *head, const int *to, const int *nx, int *order, int *parent) {
int top=0;
order[top++]=u;
parent[u]=p;
for(int i=0;i<top;i++){
  int x=order[i];
  for(int e=head[x]; e!=-1; e=nx[e]){
    int y=to[e];
    if(y==parent[x]) continue;
    if(parent[y]!=-2) continue;
    parent[y]=x;
    order[top++]=y;
  }
}
(void)top;
}

void compute_down(int n, const int *head, const int *to, const int *nx, const int *order, const int *parent, int *down) {
for(int idx=n-1; idx>=0; idx--){
  int u=order[idx];
  int top3[3]={0,0,0};
  for(int e=head[u]; e!=-1; e=nx[e]){
    int v=to[e];
    if(v==parent[u]) continue;
    int val=down[v];
    if(val>top3[0]){ top3[2]=top3[1]; top3[1]=top3[0]; top3[0]=val; }
    else if(val>top3[1]){ top3[2]=top3[1]; top3[1]=val; }
    else if(val>top3[2]){ top3[2]=val; }
  }
  int internal = 1 + top3[0] + top3[1] + top3[2];
  if(internal<1) internal=1;
  down[u] = (internal>1? internal:1);
}
}

void dfs2(int u, int p, int up, const int *head, const int *to, const int *nx, const int *down, int *best) {
int top4[4]={0,0,0,0};
for(int e=head[u]; e!=-1; e=nx[e]){
  int v=to[e];
  int val=(v==p)?up:down[v];
  if(val>top4[0]){ top4[3]=top4[2]; top4[2]=top4[1]; top4[1]=top4[0]; top4[0]=val; }
  else if(val>top4[1]){ top4[3]=top4[2]; top4[2]=top4[1]; top4[1]=val; }
  else if(val>top4[2]){ top4[3]=top4[2]; top4[2]=val; }
  else if(val>top4[3]){ top4[3]=val; }
}
int deg=0; for(int e=head[u]; e!=-1; e=nx[e]) deg++;
if(deg>=4){ int cand = 1 + top4[0]+top4[1]+top4[2]+top4[3]; if(cand>*best) *best=cand; }
for(int e=head[u]; e!=-1; e=nx[e]){
  int v=to[e]; if(v==p) continue;
  // compute up value for child v as g(u,v)
  int vals[4]={0,0,0,0}; int sz=0;
  for(int ee=head[u]; ee!=-1; ee=nx[ee]){
    int w=to[ee]; if(w==v) continue;
    int tv=(w==p)?up:down[w];
    vals[sz++]=tv;
    if(sz==4) break;
  }
  // pick top3 among all neighbors excluding v
  int t3[3]={0,0,0};
  for(int ee=head[u]; ee!=-1; ee=nx[ee]){
    int w=to[ee]; if(w==v) continue;
    int tv=(w==p)?up:down[w];
    if(tv>t3[0]){ t3[2]=t3[1]; t3[1]=t3[0]; t3[0]=tv; }
    else if(tv>t3[1]){ t3[2]=t3[1]; t3[1]=tv; }
    else if(tv>t3[2]){ t3[2]=tv; }
  }
  int upv = 1;
  if((deg-1)>=3){
    int internal=1 + t3[0]+t3[1]+t3[2];
    if(internal>upv) upv=internal;
  }
  dfs2(v,u,upv,head,to,nx,down,best);
}
}

int max_alkane(int n, const int *u, const int *v) {
int *head=(int*)malloc((size_t)n*sizeof(int));
int *to=(int*)malloc((size_t)(2*(n-1))*sizeof(int));
int *nx=(int*)malloc((size_t)(2*(n-1))*sizeof(int));
for(int i=0;i<n;i++) head[i]=-1;
int ec=0;
for(int i=0;i<n-1;i++){
  add_edge(u[i],v[i],head,to,nx,&ec);
  add_edge(v[i],u[i],head,to,nx,&ec);
}
int *order=(int*)malloc((size_t)n*sizeof(int));
int *parent=(int*)malloc((size_t)n*sizeof(int));
for(int i=0;i<n;i++) parent[i]=-2;
dfs1(0,-1,head,to,nx,order,parent);
int *down=(int*)malloc((size_t)n*sizeof(int));
compute_down(n,head,to,nx,order,parent,down);
int best=0;
dfs2(0,-1,0,head,to,nx,down,&best);
free(head); free(to); free(nx); free(order); free(parent); free(down);
return best;
}

int main(void){ int n; static int u[200005],v[200005]; read_tree(&n,u,v); int ans=max_alkane(n,u,v); printf("%d\n", ans); return 0; }
