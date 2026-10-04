#include <stdio.h>
#include <stdlib.h>

void read_input(int *n, int *m, long long *X, int *u, int *v) {
scanf("%d %d %lld", n, m, X); for(int i=0;i<*m;i++){ scanf("%d %d", &u[i], &v[i]); u[i]--; v[i]--; }
}

void build_adj(int n, int m, const int *u, const int *v, int **head1, int **to1, int **nx1, int **head2, int **to2, int **nx2) {
int *head=(int*)malloc((size_t)n*sizeof(int));
int *rhead=(int*)malloc((size_t)n*sizeof(int));
int *to=(int*)malloc((size_t)m*sizeof(int));
int *nx=(int*)malloc((size_t)m*sizeof(int));
int *rto=(int*)malloc((size_t)m*sizeof(int));
int *rnx=(int*)malloc((size_t)m*sizeof(int));
for(int i=0;i<n;i++){ head[i]=-1; rhead[i]=-1; }
int ec=0, rc=0;
for(int i=0;i<m;i++){
  int a=u[i], b=v[i];
  to[ec]=b; nx[ec]=head[a]; head[a]=ec++;
  rto[rc]=a; rnx[rc]=rhead[b]; rhead[b]=rc++;
}
*head1=head; *to1=to; *nx1=nx;
*head2=rhead; *to2=rto; *nx2=rnx;
}

long long dijkstra(int n, const int *head, const int *to, const int *nx, const int *rhead, const int *rto, const int *rnx, long long X) {
int N2=2*n;
long long INF=4000000000000000000LL;
long long *dist=(long long*)malloc((size_t)N2*sizeof(long long));
char *vis=(char*)calloc((size_t)N2,1);
for(int i=0;i<N2;i++) dist[i]=INF;
dist[0]=0;
for(;;){
  int v=-1;
  for(int i=0;i<N2;i++) if(!vis[i] && (v==-1 || dist[i]<dist[v])) v=i;
  if(v==-1) break;
  vis[v]=1;
  int x=v%n; int s=v/n;
  long long dv=dist[v];
  // toggle
  int vt=(1-s)*n + x;
  if(dv+X < dist[vt]) dist[vt]=dv+X;
  // move
  const int *H = (s==0? head : rhead);
  const int *T = (s==0? to : rto);
  const int *NX = (s==0? nx : rnx);
  for(int e=H[x]; e!=-1; e=NX[e]){
    int y=T[e];
    int u2=s*n+y;
    if(dv+1 < dist[u2]) dist[u2]=dv+1;
  }
}
long long ans = dist[n-1];
if(dist[n+(n-1)]<ans) ans=dist[n+(n-1)];
free(dist); free(vis);
return ans;
}

int main(void){ int n,m; long long X; static int u[200005], v[200005];
read_input(&n,&m,&X,u,v);
int *head,*to,*nx,*rhead,*rto,*rnx;
build_adj(n,m,u,v,&head,&to,&nx,&rhead,&rto,&rnx);
long long ans=dijkstra(n,head,to,nx,rhead,rto,rnx,X);
printf("%lld\n", ans);
free(head); free(to); free(nx); free(rhead); free(rto); free(rnx);
return 0; }
