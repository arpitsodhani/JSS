#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int *Q,long long **H,int **L,int **R){ scanf("%d%d", N,Q); *H=(long long*)malloc((size_t)(*N)*sizeof(long long)); for(int i=0;i<*N;i++) scanf("%lld", &(*H)[i]); *L=(int*)malloc((size_t)(*Q)*sizeof(int)); *R=(int*)malloc((size_t)(*Q)*sizeof(int)); for(int i=0;i<*Q;i++) scanf("%d%d", &(*L)[i], &(*R)[i]); }

long long max_between(long long *H,int l,int r){ long long m=0; for(int i=l;i<=r;i++) if(H[i]>m) m=H[i]; return m; }

int count_visible(long long *H,int N,int l,int r){
    long long midmax = max_between(H,l+1,r);
    long long curmax=0;
    int cnt=0;
    for(int j=r+1;j<N;j++){
        if(H[j]>=curmax){
            curmax=H[j];
            if(H[j]>=midmax) cnt++;
        }
    }
    return cnt;
}

void process_queries(int N,int Q,long long *H,int *L,int *R){ for(int i=0;i<Q;i++){ int l=L[i]-1, r=R[i]-1; int ans=count_visible(H,N,l,r); printf("%d\n", ans); } }

int main(void){ int N,Q; long long *H=NULL; int *L=NULL,*R=NULL; read_input(&N,&Q,&H,&L,&R); process_queries(N,Q,H,L,R); free(H); free(L); free(R); return 0; }
