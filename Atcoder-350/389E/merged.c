#include <stdio.h>
#include <stdlib.h>

void read_input(int *n,long long *M,long long *P) {
scanf("%d%lld", n,M); for(int i=0;i<*n;i++) scanf("%lld", &P[i]);
}

long long max_units(int n,long long M,long long *P) {
long long lo=0, hi=1;
for(int i=0;i<n;i++) if(P[i]<hi) hi=P[i];
hi = (long long)2e12;
while(lo<hi){
  long long mid=(lo+hi+1)/2;
  long long cost=0, cnt=0;
  for(int i=0;i<n;i++){
    long long t=(mid/P[i]+1)/2; if(t<0) t=0; if(t>0){ cnt+=t; cost+=P[i]*t*t; if(cost>M) break; }
  }
  if(cost<=M) lo=mid; else hi=mid-1;
}
long long cost=0,cnt=0; long long *next=(long long*)malloc((size_t)n*sizeof(long long));
for(int i=0;i<n;i++){ long long t=(lo/P[i]+1)/2; if(t<0) t=0; cnt+=t; cost+=P[i]*t*t; next[i]=P[i]*(2*t+1); }
for(int i=0;i<n;i++) for(int j=i+1;j<n;j++) if(next[j]<next[i]){ long long tmp=next[i]; next[i]=next[j]; next[j]=tmp; }
for(int i=0;i<n;i++){ if(cost+next[i]>M) break; cost+=next[i]; cnt++; }
free(next); return cnt;
}

void print_ll(long long x) {
printf("%lld\n", x);
}

int main(void){ int n; long long M; static long long P[200005]; read_input(&n,&M,P); long long ans=max_units(n,M,P); print_ll(ans); return 0;}
