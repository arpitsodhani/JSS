#include <stdio.h>
#include <stdlib.h>

void read_tree(int *n, long long *a, int *u, int *v) {
scanf("%d", n);
for(int i=1;i<=*n;i++) scanf("%lld", &a[i]);
for(int i=0;i<*n-1;i++){ scanf("%d %d", &u[i], &v[i]); u[i]--; v[i]--; }
}

void build_euler(int n, const int *u, const int *v, int *tin, int *tout, int *order) {
int m=n-1;
int *head=(int*)malloc((size_t)n*sizeof(int));
int *to=(int*)malloc((size_t)(2*m)*sizeof(int));
int *nx=(int*)malloc((size_t)(2*m)*sizeof(int));
for(int i=0;i<n;i++) head[i]=-1;
int ec=0;
for(int i=0;i<m;i++){ int a=u[i], b=v[i]; to[ec]=b; nx[ec]=head[a]; head[a]=ec++; to[ec]=a; nx[ec]=head[b]; head[b]=ec++; }
int *st=(int*)malloc((size_t)(2*n)*sizeof(int));
int *it=(int*)malloc((size_t)(2*n)*sizeof(int));
int top=0; int timer=0;
st[top]=0; it[top]=head[0]; tin[0]=timer; order[timer]=0; timer++; top++;
int *parent=(int*)malloc((size_t)n*sizeof(int));
for(int i=0;i<n;i++) parent[i]=-1; parent[0]=0;
while(top){
  int vtx=st[top-1];
  int e=it[top-1];
  if(e==-1){ tout[vtx]=timer; top--; continue; }
  it[top-1]=nx[e];
  int w=to[e];
  if(w==parent[vtx]) continue;
  parent[w]=vtx;
  tin[w]=timer; order[timer]=w; timer++;
  st[top]=w; it[top]=head[w]; top++;
}
free(head); free(to); free(nx); free(st); free(it); free(parent);
}

void bit_add(long long *bit, int n, int idx, long long delta) {
for(int i=idx;i<=n;i+=i&-i) bit[i]+=delta;
}

long long bit_sum(const long long *bit, int idx) {
long long s=0; for(int i=idx;i>0;i-=i&-i) s+=bit[i]; return s;
}

void process_queries(int n, const long long *a0, const int *tin, const int *tout, const int *order) {
long long *bit=(long long*)calloc((size_t)(n+2), sizeof(long long));
long long *cur=(long long*)malloc((size_t)(n+1)*sizeof(long long));
for(int i=0;i<n;i++){
  int v=order[i];
  cur[v+1]=a0[v+1];
  bit_add(bit,n,i+1,cur[v+1]);
}
int Q; scanf("%d", &Q);
for(int qi=0;qi<Q;qi++){
  int t; scanf("%d", &t);
  if(t==1){ int x; long long y; scanf("%d %lld", &x, &y); x--; int pos=tin[x]+1; long long old=cur[x+1]; cur[x+1]=y; bit_add(bit,n,pos,y-old); }
  else { int x; scanf("%d", &x); x--; int l=tin[x]+1; int r=tout[x]; long long ans=bit_sum(bit,r)-bit_sum(bit,l-1); printf("%lld\n", ans); }
}
free(bit); free(cur);
}

int main(void){ int n; static long long a[200005]; static int u[200005], v[200005]; read_tree(&n,a,u,v); int *tin=(int*)malloc((size_t)n*sizeof(int)); int *tout=(int*)malloc((size_t)n*sizeof(int)); int *order=(int*)malloc((size_t)n*sizeof(int)); build_euler(n,u,v,tin,tout,order); process_queries(n,a,tin,tout,order); free(tin); free(tout); free(order); return 0; }
