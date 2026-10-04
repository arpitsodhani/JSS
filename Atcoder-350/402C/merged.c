#include <stdio.h>

void read_input(int *n) {
scanf("%d", n);
}

long long count_pairs_even_sum(int n) {
long long even=0, odd=0;
for(int i=0;i<n;i++){
  long long x; scanf("%lld", &x);
  if((x&1LL)==0) even++; else odd++;
}
return even*(even-1)/2 + odd*(odd-1)/2;
}

void print_ll(long long v) {
printf("%lld\n", v);
}

int main(void){ int n; read_input(&n); long long ans=count_pairs_even_sum(n); print_ll(ans); return 0; }
