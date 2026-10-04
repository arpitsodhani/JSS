#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,long long **A){ scanf("%d", N); *A=(long long*)malloc((size_t)(*N)*sizeof(long long)); for(int i=0;i<*N;i++) scanf("%lld", &(*A)[i]); }

long long compute_sum(int N,long long *A) {
long long f_val(long long x){
    while((x&1LL)==0) x>>=1;
    return x;
}
long long compute_sum(int N,long long *A){
    long long ans=0;
    for(int i=0;i<N;i++){
        for(int j=i;j<N;j++){
            long long s=A[i]+A[j];
            ans += f_val(s);
        }
    }
    return ans;
}
}

void print_answer(long long ans){ printf("%lld\n", ans); }

int main(void){ int N; long long *A=NULL; read_input(&N,&A); long long ans=compute_sum(N,A); print_answer(ans); free(A); return 0; }
