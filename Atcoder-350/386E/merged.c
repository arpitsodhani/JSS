#include <stdio.h>

void read_input(int *n,int *k,long long *A) {
scanf("%d%d", n,k); for(int i=0;i<*n;i++) scanf("%lld", &A[i]);
}

long long solve(int n,int k,long long *A) {
long long best=0; long long total=0;
int idx[64]; for(int i=0;i<k;i++) idx[i]=i;
long long limit=1; for(int i=0;i<k;i++) limit=limit*(n-i)/(i+1);
while(1){
  long long x=0; for(int i=0;i<k;i++) x^=A[idx[i]]; if(x>best) best=x;
  int i=k-1; while(i>=0 && idx[i]==n-k+i) i--; if(i<0) break; idx[i]++; for(int j=i+1;j<k;j++) idx[j]=idx[j-1]+1;
}
return best;
}

void print_ll(long long x) {
printf("%lld\n", x);
}

int main(void){ int n,k; static long long A[64]; read_input(&n,&k,A); long long ans=solve(n,k,A); print_ll(ans); return 0;}
