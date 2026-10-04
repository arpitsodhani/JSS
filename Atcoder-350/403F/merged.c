#include <stdio.h>
#include <stdlib.h>

int gcd_int(int a, int b) {
int gcd_int(int a,int b){ while(b){ int t=a%b; a=b; b=t; } return a; }
}

int lcm_int(int a, int b) {
int lcm_int(int a,int b){ int g=gcd_int(a,b); return a/g*b; }
}

void solve(void){ int N,K,M; scanf("%d %d %d", &N, &K, &M); int L=lcm_int(K,M); long long *freq=(long long*)calloc((size_t)L, sizeof(long long)); long long s=0; freq[0]=1; for(int i=0;i<N;i++){ long long x; scanf("%lld", &x); s=(s+x)%L; freq[s]++; } long long ans=0; for(int r=0;r<L;r++){ long long c=freq[r]; ans += c*(c-1)/2; } printf("%lld\n", ans); free(freq); }

int main(void){ solve(); return 0; }
