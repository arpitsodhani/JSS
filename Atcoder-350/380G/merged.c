#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,long long *K,int **P){ scanf("%d%lld", N,K); *P=(int*)malloc((size_t)(*N)*sizeof(int)); for(int i=0;i<*N;i++) scanf("%d", &(*P)[i]); }

void bit_init(int N,long long *bit){ for(int i=0;i<=N;i++) bit[i]=0; }

void bit_add(int N,long long *bit,int idx,long long val){ for(int i=idx;i<=N;i+=i&-i) bit[i]+=val; }

long long bit_sum(long long *bit,int idx){ long long s=0; for(int i=idx;i>0;i-=i&-i) s+=bit[i]; return s; }

long long count_inversions(int N,int *P){
    long long inv=0;
    long long *bit=(long long*)malloc((size_t)(N+2)*sizeof(long long));
    bit_init(N,bit);
    for(int i=0;i<N;i++){
        int x=P[i];
        long long le = bit_sum(bit,x);
        inv += i - le;
        bit_add(N,bit,x,1);
    }
    free(bit);
    return inv;
}

long long mod_norm(long long v){ const long long MOD=998244353; v%=MOD; if(v<0) v+=MOD; return v; }

long long clamp_mod(long long v){ return mod_norm(v); }

long long compute_expected(int N,long long K,int *P){ long long inv=count_inversions(N,P); return clamp_mod(inv); }

void print_answer(long long ans){ printf("%lld\n", ans); }

int main(void){ int N; long long K; int *P=NULL; read_input(&N,&K,&P); long long ans=compute_expected(N,K,P); print_answer(ans); free(P); return 0; }
