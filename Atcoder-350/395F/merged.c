#include <stdio.h>
#include <stdlib.h>

void read_input(int *n, long long *X, long long *U, long long *D) {
scanf("%d %lld", n, X); for(int i=0;i<*n;i++) scanf("%lld", &U[i]); for(int i=0;i<*n;i++) scanf("%lld", &D[i]);
}

int feasible(long long H, int n, long long X, const long long *U, const long long *D) {
long long L=H-D[0]; if(L<0) L=0; long long R=U[0];
if(L>R) return 0;
for(int i=1;i<n;i++){
  long long li=H-D[i]; if(li<0) li=0;
  long long ri=U[i];
  long long nL=L-X; long long nR=R+X;
  if(nL<li) nL=li;
  if(nR>ri) nR=ri;
  if(nL>nR) return 0;
  L=nL; R=nR;
}
return 1;
}

long long max_H(int n, long long X, const long long *U, const long long *D) {
long long lo=0, hi=0;
for(int i=0;i<n;i++) if(U[i]+D[i]>hi) hi=U[i]+D[i];
hi += 1;
while(lo+1<hi){
  long long mid=(lo+hi)/2;
  if(feasible(mid,n,X,U,D)) lo=mid; else hi=mid;
}
return lo;
}

long long min_cost(int n, const long long *U, const long long *D, long long H) {
long long sum=0;
for(int i=0;i<n;i++) sum += U[i]+D[i];
return sum - (long long)n*H;
}

int main(void){ int n; long long X; long long *U=(long long*)malloc((size_t)200005*sizeof(long long)); long long *D=(long long*)malloc((size_t)200005*sizeof(long long));
read_input(&n,&X,U,D);
long long H=max_H(n,X,U,D);
long long ans=min_cost(n,U,D,H);
printf("%lld\n", ans);
free(U); free(D);
return 0; }
