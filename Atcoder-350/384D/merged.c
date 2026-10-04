#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,long long *S,long long **A){ scanf("%d%lld", N,S); *A=(long long*)malloc((size_t)(*N)*sizeof(long long)); for(int i=0;i<*N;i++) scanf("%lld", &(*A)[i]); }

int exists_subsequence(int N,long long S,long long *A){
    long long total=0; for(int i=0;i<N;i++) total+=A[i];
    if(S%total==0) return 1;
    long long target = S%total;
    int M=2*N;
    long long *B=(long long*)malloc((size_t)M*sizeof(long long));
    for(int i=0;i<M;i++) B[i]=A[i%N];
    int l=0; long long sum=0;
    for(int r=0;r<M;r++){
        sum+=B[r];
        while(sum>target && l<=r){ sum-=B[l++]; }
        if(sum==target){ free(B); return 1; }
    }
    free(B);
    return 0;
}

void print_answer(int ok){ printf("%s\n", ok?"Yes":"No"); }

int main(void){ int N; long long S; long long *A=NULL; read_input(&N,&S,&A); int ok=exists_subsequence(N,S,A); print_answer(ok); free(A); return 0; }
