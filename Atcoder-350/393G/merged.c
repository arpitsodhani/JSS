#include <stdio.h>
#include <stdlib.h>

void read_input(int *n,long long *P,long long *Q,long long *A) {
scanf("%d%lld%lld", n,P,Q); for(int i=0;i<(*n)*(*n);i++) scanf("%lld", &A[i]);
}

long long median_cost(int n,long long *A,long long *med) {
long long *tmp=(long long*)malloc((size_t)n*n*sizeof(long long));
for(int i=0;i<n*n;i++) tmp[i]=A[i];
for(int i=0;i<n*n;i++) for(int j=i+1;j<n*n;j++) if(tmp[j]<tmp[i]){ long long t=tmp[i]; tmp[i]=tmp[j]; tmp[j]=t; }
long long m=tmp[(n*n)/2]; *med=m; long long cost=0; for(int i=0;i<n*n;i++) cost += llabs(A[i]-m);
free(tmp); return cost;
}

void solve_grid(int n,long long P,long long Q,long long *A,long long *U,long long *B) {
long long med=0; long long cost=median_cost(n,A,&med);
long long budget = P/Q; // rough
if(cost<=budget){
  for(int i=0;i<n*n;i++) B[i]=med; *U=0;
} else {
  for(int i=0;i<n*n;i++) B[i]=A[i];
  long long u=0; for(int i=0;i<n;i++) for(int j=0;j<n;j++){
    if(j+1<n) u+= llabs(B[i*n+j]-B[i*n+j+1]);
    if(i+1<n) u+= llabs(B[i*n+j]-B[(i+1)*n+j]);
  }
  *U=u;
}
}

void print_grid(int n,long long U,long long *B) {
printf("%lld\n", U);
for(int i=0;i<n;i++){
  for(int j=0;j<n;j++){ if(j) printf(" "); printf("%lld", B[i*n+j]); }
  printf("\n");
}
}

int main(void){ int n; long long P,Q; static long long A[400],B[400]; long long U; read_input(&n,&P,&Q,A); solve_grid(n,P,Q,A,&U,B); print_grid(n,U,B); return 0; }
