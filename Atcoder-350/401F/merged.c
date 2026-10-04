#include <stdio.h>
#include <stdlib.h>

void read_graph(int *n, int *m, int *u, int *v) {
scanf("%d %d", n, m); for(int i=0;i<*m;i++){ scanf("%d %d", &u[i], &v[i]); u[i]--; v[i]--; }
}

int is_bipartite(int n, int m, const int *u, const int *v) {
int *head=(int*)malloc((size_t)n*sizeof(int)); int *to=(int*)malloc((size_t)2*m*sizeof(int)); int *nx=(int*)malloc((size_t)2*m*sizeof(int)); for(int i=0;i<n;i++) head[i]=-1; int ec=0; for(int i=0;i<m;i++){ int a=u[i],b=v[i]; to[ec]=b; nx[ec]=head[a]; head[a]=ec++; to[ec]=a; nx[ec]=head[b]; head[b]=ec++; }
int *col=(int*)malloc((size_t)n*sizeof(int)); for(int i=0;i<n;i++) col[i]=-1; int *q=(int*)malloc((size_t)n*sizeof(int));
for(int s=0;s<n;s++) if(col[s]<0){ int qh=0,qt=0; col[s]=0; q[qt++]=s; while(qh<qt){ int x=q[qh++]; for(int e=head[x];e!=-1;e=nx[e]){ int y=to[e]; if(col[y]<0){ col[y]=col[x]^1; q[qt++]=y; } else if(col[y]==col[x]){ free(head); free(to); free(nx); free(col); free(q); return 0; } } } }
free(head); free(to); free(nx); free(col); free(q); return 1;
}

void print_yesno(int ok) {
puts(ok?"Yes":"No");
}

int main(void){ int n,m; static int u[200005], v[200005]; read_graph(&n,&m,u,v); int ok=is_bipartite(n,m,u,v); print_yesno(ok); return 0; }
