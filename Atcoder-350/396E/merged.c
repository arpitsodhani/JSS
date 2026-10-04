#include <stdio.h>
#include <stdlib.h>

void read_input(int *n, int *m, int *x, int *y, int *z) {
scanf("%d %d", n, m); for(int i=0;i<*m;i++){ scanf("%d %d %d", &x[i], &y[i], &z[i]); x[i]--; y[i]--; }
}

void add_edge(int a, int b, int w, int *head, int *to, int *nx, int *ew, int *ec) {
to[*ec]=b; ew[*ec]=w; nx[*ec]=head[a]; head[a]=(*ec)++;
}

int build_values(int n, int m, const int *x, const int *y, const int *z, int *val, int *comp, int *comp_sz, int *comp_cnt) {
int *head=(int*)malloc((size_t)n*sizeof(int));
int *to=(int*)malloc((size_t)(2*m)*sizeof(int));
int *nx=(int*)malloc((size_t)(2*m)*sizeof(int));
int *ew=(int*)malloc((size_t)(2*m)*sizeof(int));
for(int i=0;i<n;i++){ head[i]=-1; val[i]=0; comp[i]=-1; }
int ec=0;
for(int i=0;i<m;i++){
  add_edge(x[i],y[i],z[i],head,to,nx,ew,&ec);
  add_edge(y[i],x[i],z[i],head,to,nx,ew,&ec);
}
int *q=(int*)malloc((size_t)n*sizeof(int));
int cid=0;
for(int s=0;s<n;s++) if(comp[s]==-1){
  int qh=0,qt=0; q[qt++]=s; comp[s]=cid; val[s]=0;
  int sz=0;
  while(qh<qt){
    int v=q[qh++]; sz++;
    for(int e=head[v]; e!=-1; e=nx[e]){
      int u=to[e]; int w=ew[e];
      if(comp[u]==-1){ comp[u]=cid; val[u]=val[v]^w; q[qt++]=u; }
      else { if((val[u]^val[v])!=w){ free(head); free(to); free(nx); free(ew); free(q); return 0; } }
    }
  }
  comp_sz[cid]=sz;
  cid++;
}
*comp_cnt=cid;
free(head); free(to); free(nx); free(ew); free(q);
return 1;
}

void choose_masks(int comp_cnt, const int *comp_sz, const int *comp_bit1, int *mask) {
(void)comp_bit1;
for(int i=0;i<comp_cnt;i++) mask[i]=0; (void)comp_sz;
}

void output_ans(int n, const int *val) {
for(int i=0;i<n;i++){ printf("%d%c", val[i], (i+1==n?'\n':' ')); }
}

int main(void){ int n,m; static int x[100005], y[100005], z[100005];
read_input(&n,&m,x,y,z);
int *val=(int*)malloc((size_t)n*sizeof(int));
int *comp=(int*)malloc((size_t)n*sizeof(int));
int *comp_sz=(int*)malloc((size_t)(n+1)*sizeof(int));
int comp_cnt=0;
if(!build_values(n,m,x,y,z,val,comp,comp_sz,&comp_cnt)){
  puts("-1");
  free(val); free(comp); free(comp_sz);
  return 0;
}
int *mask=(int*)calloc((size_t)comp_cnt,sizeof(int));
for(int bit=0;bit<31;bit++){
  long long ones0[300005];
  for(int c=0;c<comp_cnt;c++) ones0[c]=0;
  for(int i=0;i<n;i++) if((val[i]>>bit)&1) ones0[comp[i]]++;
  for(int c=0;c<comp_cnt;c++){
    long long sz=comp_sz[c];
    if(ones0[c] > sz-ones0[c]) mask[c] |= (1<<bit);
  }
}
for(int i=0;i<n;i++) val[i] ^= mask[comp[i]];
output_ans(n,val);
free(val); free(comp); free(comp_sz); free(mask);
return 0; }
