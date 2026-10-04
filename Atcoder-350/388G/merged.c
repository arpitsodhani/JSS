#include <stdio.h>

void read_input(int *n,int *q,long long *A,int *L,int *R) {
scanf("%d%d", n,q); for(int i=0;i<*n;i++) scanf("%lld", &A[i]); for(int i=0;i<*q;i++) scanf("%d%d", &L[i], &R[i]);
}

void answer(int n,int q,long long *A,int *L,int *R,int *out) {
for(int qi=0; qi<q; qi++){
  int l=L[qi]-1, r=R[qi]-1; int len=r-l+1; int mid=len/2;
  int i=l, j=l+mid, ans=0;
  while(i<l+mid && j<=r){ if(A[i]*2<=A[j]){ans++; i++; j++;} else j++; }
  out[qi]=ans;
}
}

void print_ans(int q,int *out) {
for(int i=0;i<q;i++) printf("%d\n", out[i]);
}

int main(void){ int n,q; static long long A[200005]; static int L[200005],R[200005],out[200005]; read_input(&n,&q,A,L,R); answer(n,q,A,L,R,out); print_ans(q,out); return 0;}
