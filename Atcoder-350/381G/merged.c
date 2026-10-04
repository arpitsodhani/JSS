#include <stdio.h>
#include <stdlib.h>

void read_input(int *T,long long **N,long long **X,long long **Y){ scanf("%d", T); *N=(long long*)malloc((size_t)(*T)*sizeof(long long)); *X=(long long*)malloc((size_t)(*T)*sizeof(long long)); *Y=(long long*)malloc((size_t)(*T)*sizeof(long long)); for(int i=0;i<*T;i++) scanf("%lld%lld%lld", &(*N)[i], &(*X)[i], &(*Y)[i]); }

long long mod_norm(long long v){ const long long MOD=998244353; v%=MOD; if(v<0) v+=MOD; return v; }

long long mul_mod(long long a,long long b){ const long long MOD=998244353; return (a%MOD)*(b%MOD)%MOD; }

void init_pair(long long x,long long y,long long *a,long long *b,long long *prod){ *a=mod_norm(x); *b=mod_norm(y); *prod=mul_mod(*a,*b); }

void advance(long long *a,long long *b,long long *prod){ const long long MOD=998244353; long long c=(*a+*b)%MOD; *prod = (*prod * c)%MOD; *a=*b; *b=c; }

long long base_case(long long n,long long x,long long y){ if(n==1) return mod_norm(x); if(n==2) return mul_mod(x,y); return -1; }

long long fib_product(long long n,long long x,long long y){
    const long long MOD=998244353;
    if(n==1) return mod_norm(x);
    if(n==2) return mul_mod(x,y);
    long long a,b,prod;
    init_pair(x,y,&a,&b,&prod);
    for(long long i=3;i<=n;i++) advance(&a,&b,&prod);
    return prod%MOD;
}

void solve_all(int T,long long *N,long long *X,long long *Y,long long *out){ for(int i=0;i<T;i++) out[i]=fib_product(N[i],X[i],Y[i]); }

void print_answers(int T,long long *out){ for(int i=0;i<T;i++) printf("%lld\n", out[i]); }

int main(void){ int T; long long *N=NULL,*X=NULL,*Y=NULL; read_input(&T,&N,&X,&Y); long long *out=(long long*)malloc((size_t)T*sizeof(long long)); solve_all(T,N,X,Y,out); print_answers(T,out); free(N); free(X); free(Y); free(out); return 0; }
