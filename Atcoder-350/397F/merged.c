#include <stdio.h>
#include <stdlib.h>

void read_input(int *n, int *a) {
scanf("%d", n); for(int i=0;i<*n;i++) scanf("%d", &a[i]);
}

int* compress(int n, int *a, int *m) {
int *b=(int*)malloc((size_t)n*sizeof(int));
for(int i=0;i<n;i++) b[i]=a[i];
for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) if(b[j]<b[i]){ int t=b[i]; b[i]=b[j]; b[j]=t; }
int k=0;
for(int i=0;i<n;i++) if(i==0||b[i]!=b[i-1]) b[k++]=b[i];
for(int i=0;i<n;i++){
  int x=a[i];
  int l=0,r=k;
  while(l<r){ int mid=(l+r)/2; if(b[mid]<x) l=mid+1; else r=mid; }
  a[i]=l;
}
*m=k;
return b;
}

void build_pref_suf(int n, const int *a, int m, int *pref, int *suf) {
int *seen=(int*)calloc((size_t)m,sizeof(int));
int cnt=0;
for(int i=0;i<n;i++){
  int x=a[i];
  if(!seen[x]){ seen[x]=1; cnt++; }
  pref[i]=cnt;
}
for(int i=0;i<m;i++) seen[i]=0;
cnt=0;
for(int i=n-1;i>=0;i--){
  int x=a[i];
  if(!seen[x]){ seen[x]=1; cnt++; }
  suf[i]=cnt;
}
free(seen);
}

void seg_add(int node, int l, int r, int ql, int qr, int val, int *mx, int *lz) {
if(ql<=l && r<=qr){ mx[node]+=val; lz[node]+=val; return; }
int mid=(l+r)/2;
if(ql<mid) seg_add(node*2,l,mid,ql,qr,val,mx,lz);
if(qr>mid) seg_add(node*2+1,mid,r,ql,qr,val,mx,lz);
int a=mx[node*2], b=mx[node*2+1];
mx[node]= (a>b?a:b) + lz[node];
}

int seg_max(int node, int l, int r, int ql, int qr, const int *mx, const int *lz) {
if(ql<=l && r<=qr) return mx[node];
int mid=(l+r)/2;
int res=-1000000000;
if(ql<mid){ int t=seg_max(node*2,l,mid,ql,qr,mx,lz); if(t>res) res=t; }
if(qr>mid){ int t=seg_max(node*2+1,mid,r,ql,qr,mx,lz); if(t>res) res=t; }
return res + lz[node];
}

int max_three_parts(int n, int *a) {
int m;
int *vals=compress(n,a,&m);
free(vals);
int *pref=(int*)malloc((size_t)n*sizeof(int));
int *suf=(int*)malloc((size_t)n*sizeof(int));
build_pref_suf(n,a,m,pref,suf);
int size=1; while(size<n+1) size<<=1;
int *mx=(int*)calloc((size_t)(size*4),sizeof(int));
int *lz=(int*)calloc((size_t)(size*4),sizeof(int));
for(int i=0;i<=n;i++){
  int base = (i==0?0:pref[i-1]);
  seg_add(1,0,n+1,i,i+1,base,mx,lz);
}
int *last=(int*)malloc((size_t)m*sizeof(int));
for(int i=0;i<m;i++) last[i]=0;
int ans=0;
for(int j=1;j<=n;j++){
  int x=a[j-1];
  int prev=last[x];
  last[x]=j;
  seg_add(1,0,n+1,prev,j,1,mx,lz);
  if(j<=1 || j>=n) continue;
  int best = seg_max(1,0,n+1,1,j,mx,lz);
  int total = best + suf[j];
  if(total>ans) ans=total;
}
free(pref); free(suf); free(mx); free(lz); free(last);
return ans;
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ int n; int *a=(int*)malloc((size_t)300000*sizeof(int)); read_input(&n,a); int ans=max_three_parts(n,a); print_int(ans); free(a); return 0; }
