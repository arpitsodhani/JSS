#include <stdio.h>

void read_input(int *n) {
scanf("%d", n);
}

long long count_partitions_even(int n) {
const long long MOD=998244353LL;
long long sum0=1, sum1=0;
int pref=0;
for(int i=0;i<n;i++){
  long long a; scanf("%lld", &a);
  pref ^= (int)(a&1LL);
  long long dp = (pref==0?sum0:sum1);
  if(pref==0) sum0 = (sum0 + dp)%MOD; else sum1=(sum1+dp)%MOD;
}
long long ans = (pref==0?sum0:sum1);
ans = (ans - 1 + MOD)%MOD;
return ans;
}

void print_ll(long long x) {
printf("%lld\n", x);
}

int main(void){ int n; read_input(&n); long long ans=count_partitions_even(n); print_ll(ans); return 0; }
