#include <stdio.h>

long long read_r(void) {
long long R; scanf("%lld", &R); return R;
}

long long isqrt_ll(long long x) {
long long lo=0, hi=x; while(lo<=hi){ long long mid=(lo+hi)/2; long long v=mid*mid; if(v==x) return mid; if(v<x) lo=mid+1; else hi=mid-1; } return hi;
}

long long count_squares(long long R) {
long long ans=0; long long R2=2*R; long long R2sq=R2*R2;
for(long long i=-R;i<=R;i++){
  long long x=2*(i<0?-i:i)+1; long long t=R2sq - x*x; if(t<0) continue;
  long long y=isqrt_ll(t); long long m=(y-1)/2; if(m<0) continue;
  ans += 2*m+1;
}
return ans;
}

void print_ll(long long x) {
printf("%lld\n", x);
}

int main(void){ long long R=read_r(); long long ans=count_squares(R); print_ll(ans); return 0;}
