#include <stdio.h>

long long read_n(void) {
long long n; scanf("%lld", &n); return n;
}

long long count_consecutive_products(long long n) {
long long lo=0,hi=2000000000LL; while(lo+1<hi){ long long mid=(lo+hi)/2; __int128 v=(__int128)mid*(mid+1); if(v<=n) lo=mid; else hi=mid; } return lo;
}

void print_ll(long long v) {
printf("%lld\n", v);
}

int main(void){ long long n=read_n(); long long ans=count_consecutive_products(n); print_ll(ans); return 0; }
