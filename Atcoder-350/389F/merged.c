#include <stdio.h>

void read_input(int *n,int *Q,int *L,int *R,int *X) {
scanf("%d%d", n,Q); for(int i=0;i<*n;i++) scanf("%d%d", &L[i], &R[i]); for(int i=0;i<*Q;i++) scanf("%d", &X[i]);
}

void simulate(int n,int Q,int *L,int *R,int *X,int *out) {
for(int qi=0;qi<Q;qi++){
  int x=X[qi];
  for(int i=0;i<n;i++) if(L[i]<=x && x<=R[i]) x++;
  out[qi]=x;
}
}

void print_ans(int Q,int *out) {
for(int i=0;i<Q;i++) printf("%d\n", out[i]);
}

int main(void){ int n,Q; static int L[200005],R[200005],X[200005],out[200005]; read_input(&n,&Q,L,R,X); simulate(n,Q,L,R,X,out); print_ans(Q,out); return 0;}
