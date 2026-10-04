#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long long mod_pow(long long a, long long e) {
long long mod_pow(long long a,long long e){ const long long MOD=998244353LL; long long r=1%MOD; while(e){ if(e&1) r=r*a%MOD; a=a*a%MOD; e>>=1; } return r; }
}

long long det_mod(long long *mat, int n) {
long long det_mod(long long *mat,int n){ const long long MOD=998244353LL; long long det=1; for(int col=0;col<n;col++){ int piv=col; while(piv<n && mat[(size_t)piv*n+col]==0) piv++; if(piv==n) return 0; if(piv!=col){ for(int j=col;j<n;j++){ long long t=mat[(size_t)col*n+j]; mat[(size_t)col*n+j]=mat[(size_t)piv*n+j]; mat[(size_t)piv*n+j]=t; } det=(MOD-det)%MOD; } long long pivot=mat[(size_t)col*n+col]%MOD; det=det*pivot%MOD; long long inv=mod_pow(pivot, MOD-2); for(int r=col+1;r<n;r++){ long long x=mat[(size_t)r*n+col]; if(!x) continue; long long f=x%MOD*inv%MOD; for(int c=col;c<n;c++){ long long v=(mat[(size_t)r*n+c] - f*mat[(size_t)col*n+c])%MOD; if(v<0) v+=MOD; mat[(size_t)r*n+c]=v; } } } return det; }
}

void solve(void){ const long long MOD=998244353LL; int N,M; scanf("%d %d", &N, &M); int n=N-1; long long *mat=(long long*)calloc((size_t)n*n, sizeof(long long)); for(int i=0;i<M;i++){ int u,v; scanf("%d %d", &u, &v); u--; v--; if(u==N-1 || v==N-1){ int x=(u==N-1)?v:u; mat[(size_t)x*n+x]=(mat[(size_t)x*n+x]+1)%MOD; } else { mat[(size_t)u*n+u]++; mat[(size_t)v*n+v]++; mat[(size_t)u*n+v]--; mat[(size_t)v*n+u]--; } }
 for(int i=0;i<n*n;i++){ mat[i]%=MOD; if(mat[i]<0) mat[i]+=MOD; }
 long long ans=det_mod(mat,n)%MOD; printf("%lld\n", ans); free(mat); }

int main(void){ solve(); return 0; }
