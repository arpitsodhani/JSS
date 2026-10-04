#include <stdio.h>
#include <stdlib.h>

void solve(void){ int N; scanf("%d", &N); int *U=(int*)malloc((size_t)(N-1)*sizeof(int)); int *V=(int*)malloc((size_t)(N-1)*sizeof(int)); char *C=(char*)malloc((size_t)(N-1)); for(int i=0;i<N-1;i++){ int a,b; char c; scanf("%d %d %c", &a, &b, &c); U[i]=a; V[i]=b; C[i]=c; } int *p=(int*)malloc((size_t)(N+1)*sizeof(int)); int *sz=(int*)malloc((size_t)(N+1)*sizeof(int)); for(int i=1;i<=N;i++){ p[i]=i; sz[i]=1; } for(int i=0;i<N-1;i++) if(C[i]=='R'){ int a=U[i], b=V[i]; while(p[a]!=a){ p[a]=p[p[a]]; a=p[a]; } while(p[b]!=b){ p[b]=p[p[b]]; b=p[b]; } if(a!=b){ if(sz[a]<sz[b]){ int t=a;a=b;b=t; } p[b]=a; sz[a]+=sz[b]; } } int Q; scanf("%d", &Q); for(int i=0;i<Q;i++){ int u,v; scanf("%d %d", &u, &v); int a=u,b=v; while(p[a]!=a){ p[a]=p[p[a]]; a=p[a]; } while(p[b]!=b){ p[b]=p[p[b]]; b=p[b]; } puts(a==b?"Yes":"No"); } free(U); free(V); free(C); free(p); free(sz); }

int main(void){ solve(); return 0; }
