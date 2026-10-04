#include <stdio.h>
#include <stdlib.h>

void read_input(int *h, int *w, int *q, int *F, int *A, int *B, int *Y, int *C, int *D, int *Z) {
scanf("%d %d", h, w);
for(int i=0;i<(*h)*(*w);i++) scanf("%d", &F[i]);
scanf("%d", q);
for(int i=0;i<*q;i++){
  scanf("%d %d %d %d %d %d", &A[i],&B[i],&Y[i],&C[i],&D[i],&Z[i]);
  A[i]--; B[i]--; C[i]--; D[i]--; 
}
}

void build_edges(int h, int w, const int *F, int *eu, int *ev, int *ew, int *m) {
int m0=0;
for(int i=0;i<h;i++){
  for(int j=0;j<w;j++){
    int id=i*w+j;
    if(i+1<h){ int id2=(i+1)*w+j; eu[m0]=id; ev[m0]=id2; int a=F[id], b=F[id2]; ew[m0]=(a<b)?a:b; m0++; }
    if(j+1<w){ int id2=i*w+(j+1); eu[m0]=id; ev[m0]=id2; int a=F[id], b=F[id2]; ew[m0]=(a<b)?a:b; m0++; }
  }
}
*m=m0;
}

void sort_edges(int m, int *eu, int *ev, int *ew) {
for(int i=0;i<m;i++){
  int best=i;
  for(int j=i+1;j<m;j++) if(ew[j]>ew[best]) best=j;
  int tu=eu[i], tv=ev[i], tw=ew[i];
  eu[i]=eu[best]; ev[i]=ev[best]; ew[i]=ew[best];
  eu[best]=tu; ev[best]=tv; ew[best]=tw;
}
}

void dsu_init(int n, int *p, int *sz) {
for(int i=0;i<n;i++){ p[i]=i; sz[i]=1; }
}

int dsu_find(int x, int *p) {
while(p[x]!=x){ p[x]=p[p[x]]; x=p[x]; } return x;
}

int dsu_unite(int a, int b, int *p, int *sz) {
a=dsu_find(a,p); b=dsu_find(b,p);
if(a==b) return 0;
if(sz[a]<sz[b]){ int t=a;a=b;b=t; }
p[b]=a; sz[a]+=sz[b]; return 1;
}

void build_mst(int n, int m, const int *eu, const int *ev, const int *ew, int *head, int *to, int *nx, int *wt) {
for(int i=0;i<n;i++) head[i]=-1;
int *p=(int*)malloc((size_t)n*sizeof(int));
int *sz=(int*)malloc((size_t)n*sizeof(int));
dsu_init(n,p,sz);
int ec=0;
for(int i=0;i<m;i++){
  if(dsu_unite(eu[i],ev[i],p,sz)){
    to[ec]=ev[i]; wt[ec]=ew[i]; nx[ec]=head[eu[i]]; head[eu[i]]=ec++; 
    to[ec]=eu[i]; wt[ec]=ew[i]; nx[ec]=head[ev[i]]; head[ev[i]]=ec++; 
  }
}
free(p); free(sz);
}

void lca_prep(int n, const int *head, const int *to, const int *nx, const int *wt, int *up, int *mn, int *dep) {
int LOG=19;
for(int i=0;i<n;i++){ dep[i]=-1; }
int *q=(int*)malloc((size_t)n*sizeof(int));
int qh=0,qt=0;
dep[0]=0; up[0*LOG+0]=0; mn[0*LOG+0]=1000000007; q[qt++]=0;
while(qh<qt){
  int v=q[qh++];
  for(int e=head[v]; e!=-1; e=nx[e]){
    int u=to[e];
    if(dep[u]!=-1) continue;
    dep[u]=dep[v]+1;
    up[u*LOG+0]=v;
    mn[u*LOG+0]=wt[e];
    q[qt++]=u;
  }
}
for(int k=1;k<LOG;k++){
  for(int v=0;v<n;v++){
    int p=up[v*LOG+(k-1)];
    up[v*LOG+k]=up[p*LOG+(k-1)];
    int a=mn[v*LOG+(k-1)], b=mn[p*LOG+(k-1)];
    mn[v*LOG+k]=(a<b)?a:b;
  }
}
free(q);
}

int bottleneck(int n, int a, int b, const int *up, const int *mn, const int *dep) {
int LOG=19;
int ans=1000000007;
if(dep[a]<dep[b]){ int t=a;a=b;b=t; }
int diff=dep[a]-dep[b];
for(int k=0;k<LOG;k++) if(diff&(1<<k)){
  int v=mn[a*LOG+k]; if(v<ans) ans=v;
  a=up[a*LOG+k];
}
if(a==b) return ans;
for(int k=LOG-1;k>=0;k--){
  if(up[a*LOG+k]!=up[b*LOG+k]){
    int va=mn[a*LOG+k]; if(va<ans) ans=va;
    int vb=mn[b*LOG+k]; if(vb<ans) ans=vb;
    a=up[a*LOG+k]; b=up[b*LOG+k];
  }
}
int va=mn[a*LOG+0]; if(va<ans) ans=va;
int vb=mn[b*LOG+0]; if(vb<ans) ans=vb;
return ans;
}

void answer_all(int h, int w, int q, const int *F, const int *A, const int *B, const int *Y, const int *C, const int *D, const int *Z, const int *up, const int *mn, const int *dep) {
for(int i=0;i<q;i++){
  int s=A[i]*w + B[i];
  int t=C[i]*w + D[i];
  int Bv=bottleneck(h*w,s,t,up,mn,dep);
  int y=Y[i], z=Z[i];
  long long ans;
  if(Bv>= (y<z?y:z)) ans = (y>z)? (y-z):(z-y);
  else ans = (long long)y + (long long)z - 2LL*Bv;
  printf("%lld\n", ans);
}
}

int main(void){ int h,w,q; int *F=(int*)malloc((size_t)250000*sizeof(int));
int *A=(int*)malloc((size_t)200005*sizeof(int));
int *B=(int*)malloc((size_t)200005*sizeof(int));
int *Y=(int*)malloc((size_t)200005*sizeof(int));
int *C=(int*)malloc((size_t)200005*sizeof(int));
int *D=(int*)malloc((size_t)200005*sizeof(int));
int *Z=(int*)malloc((size_t)200005*sizeof(int));
read_input(&h,&w,&q,F,A,B,Y,C,D,Z);
int n=h*w;
int mmax=2*n;
int *eu=(int*)malloc((size_t)mmax*sizeof(int));
int *ev=(int*)malloc((size_t)mmax*sizeof(int));
int *ew=(int*)malloc((size_t)mmax*sizeof(int));
int m=0;
build_edges(h,w,F,eu,ev,ew,&m);
sort_edges(m,eu,ev,ew);
int *head=(int*)malloc((size_t)n*sizeof(int));
int *to=(int*)malloc((size_t)(2*(n-1))*sizeof(int));
int *nx=(int*)malloc((size_t)(2*(n-1))*sizeof(int));
int *wt=(int*)malloc((size_t)(2*(n-1))*sizeof(int));
build_mst(n,m,eu,ev,ew,head,to,nx,wt);
int LOG=19;
int *up=(int*)malloc((size_t)n*(size_t)LOG*sizeof(int));
int *mn=(int*)malloc((size_t)n*(size_t)LOG*sizeof(int));
int *dep=(int*)malloc((size_t)n*sizeof(int));
lca_prep(n,head,to,nx,wt,up,mn,dep);
answer_all(h,w,q,F,A,B,Y,C,D,Z,up,mn,dep);
free(F); free(A); free(B); free(Y); free(C); free(D); free(Z);
free(eu); free(ev); free(ew);
free(head); free(to); free(nx); free(wt);
free(up); free(mn); free(dep);
return 0; }
