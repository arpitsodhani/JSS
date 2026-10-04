#include <stdio.h>
#include <stdlib.h>

void read_graph(int *n, int *m, int *u, int *v) {
scanf("%d %d", n, m); for(int i=0;i<*m;i++){ scanf("%d %d", &u[i], &v[i]); u[i]--; v[i]--; }
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

int min_delete(int n, int m, const int *u, const int *v) {
int *p=(int*)malloc((size_t)n*sizeof(int));
int *sz=(int*)malloc((size_t)n*sizeof(int));
dsu_init(n,p,sz);
int comp=n;
for(int i=0;i<m;i++) if(dsu_unite(u[i],v[i],p,sz)) comp--;
int keep = n - comp;
free(p); free(sz);
return m - keep;
}

int main(void){ int n,m; static int u[500005],v[500005]; read_graph(&n,&m,u,v); int ans=min_delete(n,m,u,v); printf("%d\n", ans); return 0; }
