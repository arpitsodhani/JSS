#include <stdio.h>
#include <stdlib.h>

void read_input(int *n,int *q,int *A,int *R,int *X) {
scanf("%d%d", n,q); for(int i=1;i<=*n;i++) scanf("%d", &A[i]); for(int i=0;i<*q;i++) scanf("%d%d", &R[i], &X[i]);
}

int compress(int n,int *A,int q,int *X,int *vals) {
int m=0; for(int i=1;i<=n;i++) vals[m++]=A[i]; for(int i=0;i<q;i++) vals[m++]=X[i];
for(int i=0;i<m;i++) for(int j=i+1;j<m;j++) if(vals[j]<vals[i]){int t=vals[i]; vals[i]=vals[j]; vals[j]=t;}
int u=0; for(int i=0;i<m;i++) if(i==0||vals[i]!=vals[i-1]) vals[u++]=vals[i];
for(int i=1;i<=n;i++){ int l=0,r=u-1; while(l<=r){int md=(l+r)/2; if(vals[md]<A[i]) l=md+1; else r=md-1;} A[i]=l+1; }
for(int i=0;i<q;i++){ int l=0,r=u-1; while(l<=r){int md=(l+r)/2; if(vals[md]<X[i]) l=md+1; else r=md-1;} X[i]=l+1; }
return u;
}

void bit_upd(int n,int *bit,int idx,int val) {
for(int i=idx;i<=n;i+=i&-i) if(bit[i]<val) bit[i]=val;
}

int bit_max(int *bit,int idx) {
int res=0; for(int i=idx;i>0;i-=i&-i) if(bit[i]>res) res=bit[i]; return res;
}

void answer_queries(int n,int q,int *A,int *R,int *X,int *ans) {
int *vals=(int*)malloc((size_t)(n+q+5)*sizeof(int));
int m=compress(n,A,q,X,vals);
int *bit=(int*)calloc((size_t)(m+2),sizeof(int));
int *ord=(int*)malloc((size_t)q*sizeof(int)); for(int i=0;i<q;i++) ord[i]=i;
for(int i=0;i<q;i++) for(int j=i+1;j<q;j++) if(R[ord[j]]<R[ord[i]]){int t=ord[i]; ord[i]=ord[j]; ord[j]=t;}
int idx=1;
for(int qi=0; qi<q; qi++){
  int id=ord[qi];
  while(idx<=R[id]){
    int v=A[idx]; int best=bit_max(bit,v-1)+1; bit_upd(m,bit,v,best); idx++;
  }
  ans[id]=bit_max(bit,X[id]);
}
free(bit); free(ord); free(vals);
}

void print_ans(int q,int *ans) {
for(int i=0;i<q;i++) printf("%d\n", ans[i]);
}

int main(void){ int n,q; static int A[200005],R[200005],X[200005],ans[200005]; read_input(&n,&q,A,R,X); answer_queries(n,q,A,R,X,ans); print_ans(q,ans); return 0; }
