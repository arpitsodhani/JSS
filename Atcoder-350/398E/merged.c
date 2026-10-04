#include <stdio.h>
#include <stdlib.h>

void read_tree(int *n, int *u, int *v) {
scanf("%d", n); for(int i=0;i<*n-1;i++){ scanf("%d %d", &u[i], &v[i]); u[i]--; v[i]--; }
}

void bipartition(int n, const int *u, const int *v, int *col) {
int m=n-1;
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
int qh=0, qt=0;
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

int find_move(int n, const int *col, char *used, int *out_a, int *out_b) {
for(int i=0;i<n;i++) for(int j=i+1;j<n;j++){
  if(col[i]==col[j]) continue;
  int idx=i*n+j;
  if(!used[idx]){ used[idx]=1; *out_a=i; *out_b=j; return 1; }
}
return 0;
}

void play_game(int n, const int *col, const char *adj) {
(void)adj;
char *used=(char*)calloc((size_t)n*(size_t)n,1);
int total=0;
for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) if(col[i]!=col[j]) total++;
int edges=n-1;
int moves=total-edges;
if(moves%2==1){
  puts("First"); fflush(stdout);
  int a,b;
  while(find_move(n,col,used,&a,&b)){
    printf("%d %d\n", a+1,b+1); fflush(stdout);
    int x,y; if(scanf("%d %d", &x,&y)!=2) break; if(x==-1) break;
    x--; y--; if(x>y){ int t=x;x=y;y=t; }
    used[x*n+y]=1;
  }
} else {
  puts("Second"); fflush(stdout);
  for(;;){
    int x,y; if(scanf("%d %d", &x,&y)!=2) break; if(x==-1) break;
    x--; y--; if(x>y){ int t=x;x=y;y=t; }
    used[x*n+y]=1;
    int a,b; if(!find_move(n,col,used,&a,&b)) break;
    printf("%d %d\n", a+1,b+1); fflush(stdout);
  }
}
free(used);
}

int main(void){ int n; static int u[205],v[205]; read_tree(&n,u,v); int *col=(int*)malloc((size_t)n*sizeof(int)); static char adj_dummy=0; bipartition(n,u,v,col); play_game(n,col,&adj_dummy); free(col); return 0; }
