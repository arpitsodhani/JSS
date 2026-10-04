#include <stdio.h>
#include <stdlib.h>

void read_input(int *n, int *m, int *c, int *u, int *v, int *col, int *a) {
scanf("%d %d %d", n, m, c);
for(int i=1;i<=*c;i++) scanf("%d", &a[i]);
for(int i=0;i<*m;i++){ scanf("%d %d %d", &u[i], &v[i], &col[i]); u[i]--; v[i]--; }
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

int can_spanning(int n, int m, int L, int R, const int *u, const int *v, const int *col, const int *A, int C) {
int need=n-1;
int *p=(int*)malloc((size_t)n*sizeof(int));
int *sz=(int*)malloc((size_t)n*sizeof(int));
dsu_init(n,p,sz);
int *used=(int*)calloc((size_t)(C+1),sizeof(int));
int got=0;
for(int i=0;i<m && got<need;i++){
  int cc=col[i]; if(cc<L||cc>R) continue;
  if(used[cc]>=A[cc]) continue;
  if(dsu_unite(u[i],v[i],p,sz)){
    used[cc]++; got++;
  }
}
free(p); free(sz); free(used);
return got==need;
}

long long count_ranges(int n, int m, int C, const int *u, const int *v, const int *col, const int *A) {
long long ans=0;
for(int L=1;L<=C;L++){
  for(int R=L;R<=C;R++){
    if(can_spanning(n,m,L,R,u,v,col,A,C)) ans++; 
  }
}
return ans;
}

int main(void){ int n,m,C; static int A[305]; static int u[500005], v[500005], col[500005]; read_input(&n,&m,&C,u,v,col,A); long long ans=count_ranges(n,m,C,u,v,col,A); printf("%lld\n", ans); return 0; }
