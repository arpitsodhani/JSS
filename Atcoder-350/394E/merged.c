#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int read_n(void) {
int n; scanf("%d", &n); return n;
}

void build_graph(int n, char *C, int **rev_head, int **rev_to, int **rev_nx, int **rev_ch, int **fwd_head, int **fwd_to, int **fwd_nx, int **fwd_ch) {
int m=0;
for(int i=0;i<n*n;i++) if(C[i]!='-') m++;
int *rh=(int*)malloc((size_t)n*sizeof(int));
int *fh=(int*)malloc((size_t)n*sizeof(int));
int *rto=(int*)malloc((size_t)m*sizeof(int));
int *rn=(int*)malloc((size_t)m*sizeof(int));
int *rch=(int*)malloc((size_t)m*sizeof(int));
int *fto=(int*)malloc((size_t)m*sizeof(int));
int *fn=(int*)malloc((size_t)m*sizeof(int));
int *fch=(int*)malloc((size_t)m*sizeof(int));
for(int i=0;i<n;i++){ rh[i]=-1; fh[i]=-1; }
int ec=0;
for(int i=0;i<n;i++){
  for(int j=0;j<n;j++){
    char ch=C[i*n+j];
    if(ch=='-') continue;
    // forward i->j
    fto[ec]=j; fch[ec]=ch-'a'; fn[ec]=fh[i]; fh[i]=ec;
    // reverse edge into j: i->j means incoming to j from i
    rto[ec]=i; rch[ec]=ch-'a'; rn[ec]=rh[j]; rh[j]=ec;
    ec++;
  }
}
*rev_head=rh; *rev_to=rto; *rev_nx=rn; *rev_ch=rch;
*fwd_head=fh; *fwd_to=fto; *fwd_nx=fn; *fwd_ch=fch;
}

void pal_bfs(int n, const int *rev_head, const int *rev_to, const int *rev_nx, const int *rev_ch, const int *fwd_head, const int *fwd_to, const int *fwd_nx, const int *fwd_ch, int *dist) {
int N=n*n;
for(int i=0;i<N;i++) dist[i]=-1;
int *q=(int*)malloc((size_t)N*sizeof(int));
int qh=0, qt=0;
for(int i=0;i<n;i++){
  dist[i*n+i]=0;
  q[qt++]=i*n+i;
}
for(int a=0;a<n;a++){
  for(int e=fwd_head[a]; e!=-1; e=fwd_nx[e]){
    int b=fwd_to[e];
    if(dist[a*n+b]==-1){ dist[a*n+b]=1; q[qt++]=a*n+b; }
  }
}
while(qh<qt){
  int s=q[qh++];
  int i=s/n, j=s%n;
  int d=dist[s];
  for(int ie=rev_head[i]; ie!=-1; ie=rev_nx[ie]){
    int u=rev_to[ie]; int c=rev_ch[ie];
    for(int je=fwd_head[j]; je!=-1; je=fwd_nx[je]){
      if(fwd_ch[je]!=c) continue;
      int v=fwd_to[je];
      int ns=u*n+v;
      if(dist[ns]==-1){ dist[ns]=d+2; q[qt++]=ns; }
    }
  }
}
free(q);
}

void print_all(int n, const int *dist) {
for(int i=0;i<n;i++){
  for(int j=0;j<n;j++){
    if(j) putchar(' ');
    printf("%d", dist[i*n+j]);
  }
  putchar('\n');
}
}

int main(void){ int n=read_n();
char *C=(char*)malloc((size_t)n*(size_t)n);
for(int i=0;i<n;i++){
  char buf[205]; scanf("%s", buf);
  for(int j=0;j<n;j++) C[i*n+j]=buf[j];
}
int *rh,*rto,*rn,*rch,*fh,*fto,*fn,*fch;
build_graph(n,C,&rh,&rto,&rn,&rch,&fh,&fto,&fn,&fch);
int *dist=(int*)malloc((size_t)n*(size_t)n*sizeof(int));
pal_bfs(n,rh,rto,rn,rch,fh,fto,fn,fch,dist);
print_all(n,dist);
free(C); free(rh); free(rto); free(rn); free(rch); free(fh); free(fto); free(fn); free(fch); free(dist);
return 0; }
