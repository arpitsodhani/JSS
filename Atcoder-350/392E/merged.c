#include <stdio.h>
#include <stdlib.h>

void read_input(int *n,int *m,int *U,int *V) {
scanf("%d%d", n,m); for(int i=0;i<*m;i++) scanf("%d%d", &U[i], &V[i]);
}

int find(int x,int *p) {
if(p[x]==x) return x; p[x]=find(p[x],p); return p[x];
}

int unite(int a,int b,int *p,int *r) {
a=find(a,p); b=find(b,p); if(a==b) return 0; if(r[a]<r[b]){int t=a;a=b;b=t;} p[b]=a; if(r[a]==r[b]) r[a]++; return 1;
}

int build_ops(int n,int m,int *U,int *V,int *ops) {
int *p=(int*)malloc((size_t)(n+1)*sizeof(int));
int *r=(int*)calloc((size_t)(n+1),sizeof(int));
for(int i=1;i<=n;i++) p[i]=i;
int *extra=(int*)malloc((size_t)m*sizeof(int)); int ec=0;
for(int i=0;i<m;i++){
  if(!unite(U[i],V[i],p,r)) extra[ec++]=i;
}
int *rep=(int*)malloc((size_t)(n+1)*sizeof(int)); int rc=0;
for(int i=1;i<=n;i++) if(find(i,p)==i) rep[rc++]=i;
int opk=0;
for(int i=1;i<rc;i++){
  int ei=extra[i-1];
  ops[3*opk]=ei+1; ops[3*opk+1]=rep[0]; ops[3*opk+2]=rep[i]; opk++;
}
free(rep); free(extra); free(p); free(r); return opk;
}

void print_ops(int k,int *ops) {
printf("%d\n", k); for(int i=0;i<k;i++) printf("%d %d %d\n", ops[3*i], ops[3*i+1], ops[3*i+2]);
}

int main(void){ int n,m; static int U[200005],V[200005]; read_input(&n,&m,U,V); static int ops[600005]; int k=build_ops(n,m,U,V,ops); print_ops(k,ops); return 0; }
