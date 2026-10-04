#include <stdio.h>
#include <stdlib.h>

void read_input(long long *N){ scanf("%lld", N); }

long long count_nine_divisors(long long N) {
int is_prime(int x){
    if(x<2) return 0;
    for(int i=2; (long long)i*i<=x; i++) if(x%i==0) return 0;
    return 1;
}
long long count_nine_divisors(long long N){
    long long ans=0;
    int limit=2000000;
    char *isprime=(char*)malloc((size_t)(limit+1));
    for(int i=0;i<=limit;i++) isprime[i]=1;
    isprime[0]=isprime[1]=0;
    for(int i=2;i*i<=limit;i++) if(isprime[i]) for(int j=i*i;j<=limit;j+=i) isprime[j]=0;
    int *pr=(int*)malloc((size_t)(limit+1)*sizeof(int));
    int pc=0;
    for(int i=2;i<=limit;i++) if(isprime[i]) pr[pc++]=i;
    // p^8
    for(int i=0;i<pc;i++){
        long long p=pr[i];
        long long v=1;
        for(int k=0;k<8;k++){ if(v> N/p) { v=N+1; break; } v*=p; }
        if(v<=N) ans++;
        else break;
    }
    // p^2 q^2
    for(int i=0;i<pc;i++){
        long long p=pr[i];
        long long p2=p*p;
        if(p2> N) break;
        for(int j=i+1;j<pc;j++){
            long long q=pr[j];
            long long q2=q*q;
            if(p2> N/q2) break;
            if(p2*q2<=N) ans++;
        }
    }
    free(isprime); free(pr);
    return ans;
}
}

void print_answer(long long ans){ printf("%lld\n", ans); }

int main(void){ long long N; read_input(&N); long long ans=count_nine_divisors(N); print_answer(ans); return 0; }
