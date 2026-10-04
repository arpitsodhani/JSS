#include <stdio.h>

int read_input(long long *A) {
int n; scanf("%d", &n); for(int i=0;i<n;i++) scanf("%lld", &A[i]); return n;
}

int max_pairs(int n,long long *A) {
int mid=n/2; int i=0,j=mid,ans=0;
while(i<mid && j<n){
  if(A[i]*2<=A[j]){ ans++; i++; j++; }
  else j++;
}
return ans;
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ static long long A[200005]; int n=read_input(A); int ans=max_pairs(n,A); print_int(ans); return 0;}
