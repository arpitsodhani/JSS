#include <stdio.h>

void read_input(int *n,int *P,int *Q) {
scanf("%d", n); for(int i=1;i<=*n;i++) scanf("%d", &P[i]); for(int i=1;i<=*n;i++) scanf("%d", &Q[i]);
}

void build_inv(int n,int *Q,int *inv) {
for(int i=1;i<=n;i++) inv[Q[i]]=i;
}

void build_ans(int n,int *P,int *Q,int *inv,int *ans) {
for(int bib=1;bib<=n;bib++){ int person=inv[bib]; int target=P[person]; ans[bib]=Q[target]; }
}

void print_ans(int n,int *ans) {
for(int i=1;i<=n;i++){ if(i>1) printf(" "); printf("%d", ans[i]); } printf("\n");
}

int main(void){ int n; static int P[200005],Q[200005],inv[200005],ans[200005]; read_input(&n,P,Q); build_inv(n,Q,inv); build_ans(n,P,Q,inv,ans); print_ans(n,ans); return 0; }
