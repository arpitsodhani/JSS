#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_graph(int *n, int *m, int *k, int *u, int *v) {
scanf("%d %d %d", n, m, k); for(int i=0;i<*m;i++){ scanf("%d %d", &u[i], &v[i]); u[i]--; v[i]--; }
}

int shortest_01(int n, int m, const int *u, const int *v, const char *w) {
int INF=1e9;
int *head=(int*)malloc((size_t)n*sizeof(int));
int *to=(int*)malloc((size_t)m*sizeof(int));
int *nx=(int*)malloc((size_t)m*sizeof(int));
for(int i=0;i<n;i++) head[i]=-1;
for(int i=0;i<m;i++){ to[i]=v[i]; nx[i]=head[u[i]]; head[u[i]]=i; }
int *dist=(int*)malloc((size_t)n*sizeof(int));
for(int i=0;i<n;i++) dist[i]=INF;
int *dq=(int*)malloc((size_t)(2*n+5)*sizeof(int));
int headq=n, tailq=n;
dist[0]=0; dq[headq]=0;
while(headq<=tailq){
  int x=dq[headq++];
  int dx=dist[x];
  for(int e=head[x]; e!=-1; e=nx[e]){
    int y=to[e];
    int nd=dx + (w[e]?1:0);
    if(nd<dist[y]){
      dist[y]=nd;
      if(w[e]) dq[++tailq]=y; else dq[--headq]=y;
    }
  }
}
int ans=dist[n-1];
free(head); free(to); free(nx); free(dist); free(dq);
return ans;
}

int improve_once(int n, int m, int k, const int *u, const int *v, char *w, char *chosen) {
int INF=1e9;
int V=n;
int *head=(int*)malloc((size_t)V*sizeof(int));
int *to=(int*)malloc((size_t)m*sizeof(int));
int *nx=(int*)malloc((size_t)m*sizeof(int));
for(int i=0;i<V;i++) head[i]=-1;
for(int i=0;i<m;i++){ to[i]=v[i]; nx[i]=head[u[i]]; head[u[i]]=i; }
int *dist=(int*)malloc((size_t)V*sizeof(int));
int *pre_v=(int*)malloc((size_t)V*sizeof(int));
int *pre_e=(int*)malloc((size_t)V*sizeof(int));
for(int i=0;i<V;i++){ dist[i]=INF; pre_v[i]=-1; pre_e[i]=-1; }
int *dq=(int*)malloc((size_t)(2*V+5)*sizeof(int));
int hq=V,tq=V;
dist[0]=0; dq[hq]=0;
while(hq<=tq){
  int x=dq[hq++];
  for(int e=head[x]; e!=-1; e=nx[e]){
    int y=to[e];
    int nd=dist[x] + (w[e]?1:0);
    if(nd<dist[y]){
      dist[y]=nd; pre_v[y]=x; pre_e[y]=e;
      if(w[e]) dq[++tq]=y; else dq[--hq]=y;
    }
  }
}
int cur=n-1;
int flipped=0;
while(cur!=0 && pre_v[cur]!=-1){
  int e=pre_e[cur];
  if(!w[e] && !chosen[e]){
    chosen[e]=1; flipped++; if(flipped==k) break;
  }
  cur=pre_v[cur];
}
for(int i=0;i<m;i++) if(chosen[i]) w[i]=1;
free(head); free(to); free(nx); free(dist); free(pre_v); free(pre_e); free(dq);
return flipped;
}

int maximize_distance(int n, int m, int k, const int *u, const int *v) {
char *w=(char*)calloc((size_t)m,sizeof(char));
char *chosen=(char*)calloc((size_t)m,sizeof(char));
int picked=0;
for(int it=0; it<200 && picked<k; it++){
  int add=improve_once(n,m,k-picked,u,v,w,chosen);
  if(add==0) break;
  picked += add;
}
for(int i=0;i<m && picked<k;i++) if(!chosen[i]){ chosen[i]=1; w[i]=1; picked++; }
int ans=shortest_01(n,m,u,v,w);
free(w); free(chosen);
return ans;
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ int n,m,k; static int u[105], v[105]; read_graph(&n,&m,&k,u,v); int ans=maximize_distance(n,m,k,u,v); print_int(ans); return 0; }
