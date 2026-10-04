#include <stdio.h>
#include <stdlib.h>

int read_input(int *A) {
int n; scanf("%d", &n); for(int i=0;i<n;i++) scanf("%d", &A[i]); return n;
}

long long calc_sum(int n,int *A) {
long long ans=0;
for(int L=0;L<n;L++){
  int freq[105]={0};
  for(int R=L;R<n;R++){
    freq[A[R]]++;
    int ops=0; int i=0;
    while(i<105){ while(i<105 && freq[i]==0) i++; if(i>=105) break; int j=i; while(j+1<105 && freq[j+1]>0) j++; ops++; i=j+1; }
    ans+=ops;
  }
}
return ans;
}

void print_ll(long long x) {
printf("%lld\n", x);
}

int main(void){ static int A[505]; int n=read_input(A); long long ans=calc_sum(n,A); print_ll(ans); return 0;}
