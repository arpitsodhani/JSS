#include <stdio.h>

void read_input(int *N,int *Q,int *q,int *r,int *t,long long *d){ scanf("%d", N); for(int i=0;i<*N;i++) scanf("%d%d", &q[i], &r[i]); scanf("%d", Q); for(int i=0;i<*Q;i++) scanf("%d%lld", &t[i], &d[i]); }

long long next_day(long long d,int q,int r){ int mod = d%q; if(mod<=r) return d + (r-mod); return d + (q - (mod-r)); }

void process(int N,int Q,int *q,int *r,int *t,long long *d){ for(int i=0;i<Q;i++){ int idx=t[i]-1; long long ans=next_day(d[i],q[idx],r[idx]); printf("%lld\n", ans); } }

int main(void){ int N,Q; int q[105], r[105], t[105]; long long d[105]; read_input(&N,&Q,q,r,t,d); process(N,Q,q,r,t,d); return 0; }
