#include <stdio.h>
#include <stdlib.h>

void read_input(int *n,long long *S) {
scanf("%d", n); for(int i=0;i<*n;i++) scanf("%lld", &S[i]);
}

long long count_triplets(int n,long long *S) {
long long ans=0;
for(int j=0;j<n;j++){
  for(int i=0;i<n;i++) if(S[i]<S[j]){
    long long c=2*S[j]-S[i];
    for(int k=0;k<n;k++) if(S[k]==c) ans++;
  }
}
return ans/1;
}

void print_ll(long long x) {
printf("%lld\n", x);
}

int main(void){ int n; long long S[70]; read_input(&n,S); long long ans=count_triplets(n,S); print_ll(ans); return 0; }
