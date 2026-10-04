#include <stdio.h>
#include <string.h>

void solve(void){
  enum{MAXA=1000000};
  static int freq[MAXA+1];
  static int mu[MAXA+1];
  static int primes[MAXA/10];
  static int lp[MAXA+1];
  int N; scanf("%d", &N);
  memset(freq,0,sizeof(freq));
  for(int i=0;i<N;i++){ int x; scanf("%d", &x); freq[x]++; }
  int pc=0; mu[1]=1; for(int i=2;i<=MAXA;i++) lp[i]=0;
  for(int i=2;i<=MAXA;i++){
    if(lp[i]==0){ lp[i]=i; primes[pc++]=i; mu[i]=-1; }
    for(int j=0;j<pc;j++){
      int p=primes[j]; long long v=(long long)p*i; if(v>MAXA) break;
      lp[v]=p;
      if(i%p==0){ mu[v]=0; break; } else mu[v]=-mu[i];
    }
  }
  static int cnt[MAXA+1];
  for(int d=1;d<=MAXA;d++) cnt[d]=0;
  for(int d=1;d<=MAXA;d++) for(int m=d;m<=MAXA;m+=d) cnt[d]+=freq[m];
  long long gcd1=0;
  for(int d=1;d<=MAXA;d++) if(mu[d]){ long long c=cnt[d]; gcd1 += (long long)mu[d] * (c*(c-1)/2); }
  long long total=(long long)N*(N-1)/2;
  printf("%lld\n", total - gcd1);
}

int main(void){ solve(); return 0; }
