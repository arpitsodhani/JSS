#include <stdio.h>

long long read_n(void) {
long long n; scanf("%lld", &n); return n;
}

long long count_good(long long n) {
long long ans=0;
for(long long b=1;b*b<=n;b++){
  long long sq=b*b;
  long long x=sq;
  while(x<=n){ ans++; if(x>n/2) break; x*=2; }
}
return ans;
}

int main(void){ long long n=read_n(); long long ans=count_good(n); printf("%lld\n", ans); return 0; }
