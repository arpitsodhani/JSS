#include <stdio.h>

int read_n(void) {
int n; scanf("%d", &n); return n;
}

long long max_manhattan(int n) {
long long max1=-4000000000000000000LL, min1=4000000000000000000LL;
long long max2=-4000000000000000000LL, min2=4000000000000000000LL;
for(int i=0;i<n;i++){
  long long x,y; scanf("%lld %lld", &x, &y);
  long long s1=x+y; long long s2=x-y;
  if(s1>max1) max1=s1; if(s1<min1) min1=s1;
  if(s2>max2) max2=s2; if(s2<min2) min2=s2;
}
long long d1=max1-min1; long long d2=max2-min2;
return d1>d2?d1:d2;
}

void print_ll(long long v) {
printf("%lld\n", v);
}

int main(void){ int n=read_n(); long long ans=max_manhattan(n); print_ll(ans); return 0; }
