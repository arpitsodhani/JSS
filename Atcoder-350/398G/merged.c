#include <stdio.h>
#include <stdlib.h>

void read_graph(int *n, int *m, int *u, int *v) {
scanf("%d %d", n, m); for(int i=0;i<*m;i++){ scanf("%d %d", &u[i], &v[i]); u[i]--; v[i]--; }
}

void bipartition(int n, int m, const int *u, const int *v, int *col) {
int *head=(int*)malloc((size_t)n*sizeof(int));
int *to=(int*)malloc((size_t)(2*m)*sizeof(int));
int *nx=(int*)malloc((size_t)(2*m)*sizeof(int));
for(int i=0;i<n;i++) head[i]=-1;
int ec=0;
for(int i=0;i<m;i++){
  int a=u[i], b=v[i];
  to[ec]=b; nx[ec]=head[a]; head[a]=ec++;
  to[ec]=a; nx[ec]=head[b]; head[b]=ec++;
}
for(int i=0;i<n;i++) col[i]=-1;
int *q=(int*)malloc((size_t)n*sizeof(int));
int qh=0,qt=0;
col[0]=0; q[qt++]=0;
while(qh<qt){
  int x=q[qh++];
  for(int e=head[x]; e!=-1; e=nx[e]){
    int y=to[e];
    if(col[y]==-1){ col[y]=col[x]^1; q[qt++]=y; }
  }
}
free(head); free(to); free(nx); free(q);
}

long long count_moves(int n, int m, const int *u, const int *v, const int *col) {
long long L=0,R=0;
for(int i=0;i<n;i++) if(col[i]==0) L++; else R++;
long long total=L*R;
return total - (long long)m;
}

const char* winner(long long moves) {
return (moves%2)?"Aoki":"Takahashi";
}

int main(void){ int n,m; static int u[200005], v[200005]; read_graph(&n,&m,u,v); int *col=(int*)malloc((size_t)n*sizeof(int)); bipartition(n,m,u,v,col); long long moves=count_moves(n,m,u,v,col); puts(winner(moves)); free(col); return 0; }
