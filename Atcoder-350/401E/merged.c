#include <stdio.h>
#include <stdlib.h>

void read_items(int *n, long long *X, long long *Y, long long *A, long long *B) {
scanf("%d %lld %lld", n, X, Y); for(int i=0;i<*n;i++) scanf("%lld %lld", &A[i], &B[i]);
}

long long best_satisfaction(int n, long long X, long long Y, const long long *A, const long long *B) {
// Heuristic: choose all items with positive (A - Y*B) for overspend case; compare with best single item and empty.
long long best=0;
for(int i=0;i<n;i++) if(A[i]>best) best=A[i];
long long sumv=0, sumc=0;
for(int i=0;i<n;i++){
  __int128 d=(__int128)A[i] - (__int128)Y*B[i];
  if(d>0){ sumv += (long long)d; sumc += B[i]; }
}
if(sumc > X){
  long long cand = (long long)((__int128)X*Y + sumv);
  if(cand>best) best=cand;
}
return best;
}

void print_ll(long long x) {
printf("%lld\n", x);
}

int main(void){ int n; long long X,Y; static long long A[200005], B[200005]; read_items(&n,&X,&Y,A,B); long long ans=best_satisfaction(n,X,Y,A,B); print_ll(ans); return 0; }
