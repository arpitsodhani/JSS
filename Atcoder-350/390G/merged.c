#include <stdio.h>
#include <stdlib.h>

int read_n(void) {
int n; scanf("%d", &n); return n;
}

long long sum_perm(int n) {
const long long MOD=998244353LL;
if(n>8) return 0;
int *perm=(int*)malloc((size_t)n*sizeof(int)); for(int i=0;i<n;i++) perm[i]=i+1;
long long ans=0;
do{
  long long val=0; for(int i=0;i<n;i++){ int x=perm[i]; long long t=x; long long pow=1; while(pow<=t/10) pow*=10; val=val*(pow*10)%MOD; val=(val+x)%MOD; }
  ans=(ans+val)%MOD;
  int k=n-2; while(k>=0 && perm[k]>perm[k+1]) k--; if(k<0) break; int l=n-1; while(perm[l]<perm[k]) l--; int tmp=perm[k]; perm[k]=perm[l]; perm[l]=tmp; for(int i=k+1,j=n-1;i<j;i++,j--){ tmp=perm[i]; perm[i]=perm[j]; perm[j]=tmp; }
}while(1);
free(perm); return ans;
}

void print_ll(long long x) {
printf("%lld\n", x);
}

int main(void){ int n=read_n(); long long ans=sum_perm(n); print_ll(ans); return 0;}
