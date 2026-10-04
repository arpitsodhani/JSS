#include <stdio.h>
#include <stdlib.h>

int read_input(long long *X,long long *H) {
int n; scanf("%d", &n); for(int i=0;i<n;i++) scanf("%lld%lld", &X[i], &H[i]); return n;
}

int can_see_all(int n,long long *X,long long *H,long long h) {
for(int i=0;i<n;i++){
  int ok=1;
  for(int j=0;j<n;j++) if(X[j]>0 && X[j]<X[i]){
    long double y = (long double)h + (long double)(H[i]-h)*(long double)X[j]/(long double)X[i];
    if(y <= H[j]+1e-12L){ ok=0; break; }
  }
  if(!ok) return 0;
}
return 1;
}

long long solve(int n,long long *X,long long *H) {
if(can_see_all(n,X,H,0)) return -1;
long long lo=0, hi=1000000000LL, ans=0;
while(lo<=hi){ long long mid=(lo+hi)/2; if(can_see_all(n,X,H,mid)){ hi=mid-1; } else { ans=mid; lo=mid+1; } }
return ans;
}

void print_ll(long long x) {
printf("%lld\n", x);
}

int main(void){ static long long X[200005],H[200005]; int n=read_input(X,H); long long ans=solve(n,X,H); print_ll(ans); return 0;}
