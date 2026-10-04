#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_input(int *n, long long *a) {
scanf("%d", n); for(int i=0;i<*n;i++) scanf("%lld", &a[i]);
}

long long count_good(int n, const long long *a) {
const int B=450; long long ans=0; static long long pref[200005+1]; pref[0]=0; for(int i=0;i<n;i++) pref[i+1]=pref[i]+a[i];
for(int len=1;len<=B;len++){
  static int cnt[451]; memset(cnt,0,sizeof(cnt));
  // Use modulo len on prefix; subarray [l,r) sum divisible by len iff pref[r]%len == pref[l]%len.
  for(int i=0;i<=n;i++){
    int r=(int)(pref[i]%len); if(r<0) r+=len;
    ans += cnt[r]; cnt[r]++;
  }
}
for(int len=B+1;len<=n;len++){
  for(int l=0;l+len<=n;l++){
    long long s=pref[l+len]-pref[l];
    if(s%len==0) ans++;
  }
}
return ans;
}

void print_ll(long long v) {
printf("%lld\n", v);
}

int main(void){ int n; static long long a[200005]; read_input(&n,a); long long ans=count_good(n,a); print_ll(ans); return 0; }
