#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int *K,long long **A,long long **B,int **X,int **Y){ scanf("%d", N); *A=(long long*)malloc((size_t)(*N)*sizeof(long long)); *B=(long long*)malloc((size_t)(*N)*sizeof(long long)); for(int i=0;i<*N;i++) scanf("%lld", &(*A)[i]); for(int i=0;i<*N;i++) scanf("%lld", &(*B)[i]); scanf("%d", K); *X=(int*)malloc((size_t)(*K)*sizeof(int)); *Y=(int*)malloc((size_t)(*K)*sizeof(int)); for(int i=0;i<*K;i++) scanf("%d%d", &(*X)[i], &(*Y)[i]); }

long long sum_abs_prefix(long long *A,int x,long long *B,int y){
    long long *AA=(long long*)malloc((size_t)x*sizeof(long long));
    long long *BB=(long long*)malloc((size_t)y*sizeof(long long));
    for(int i=0;i<x;i++) AA[i]=A[i];
    for(int i=0;i<y;i++) BB[i]=B[i];
    for(int i=0;i<x;i++) for(int j=i+1;j<x;j++) if(AA[j]<AA[i]){ long long t=AA[i]; AA[i]=AA[j]; AA[j]=t; }
    for(int i=0;i<y;i++) for(int j=i+1;j<y;j++) if(BB[j]<BB[i]){ long long t=BB[i]; BB[i]=BB[j]; BB[j]=t; }
    long long ans=0;
    int i=0,j=0;
    while(i<x && j<y){
        if(AA[i]<BB[j]){ ans += (long long)(y-j)* (BB[j]-AA[i]); i++; }
        else { ans += (long long)(x-i)* (AA[i]-BB[j]); j++; }
    }
    free(AA); free(BB);
    return ans;
}

void print_queries(int K,int *X,int *Y,long long *A,long long *B){ for(int i=0;i<K;i++){ long long ans=sum_abs_prefix(A,X[i],B,Y[i]); printf("%lld\n", ans); } }

int main(void){ int N,K; long long *A=NULL,*B=NULL; int *X=NULL,*Y=NULL; read_input(&N,&K,&A,&B,&X,&Y); print_queries(K,X,Y,A,B); free(A); free(B); free(X); free(Y); return 0; }
