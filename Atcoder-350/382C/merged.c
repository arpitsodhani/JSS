#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int *M,long long **A,long long **B){ scanf("%d%d", N,M); *A=(long long*)malloc((size_t)(*N)*sizeof(long long)); *B=(long long*)malloc((size_t)(*M)*sizeof(long long)); for(int i=0;i<*N;i++) scanf("%lld", &(*A)[i]); for(int j=0;j<*M;j++) scanf("%lld", &(*B)[j]); }

int earliest_eater(int N,long long *A,long long b){
    int l=0,r=N-1,ans=-1;
    while(l<=r){
        int m=(l+r)/2;
        if(A[m]<=b){ ans=m; r=m-1; }
        else l=m+1;
    }
    return ans;
}

void process_all(int N,int M,long long *A,long long *B,int *out){
    for(int i=0;i<M;i++){
        int idx=earliest_eater(N,A,B[i]);
        out[i]= (idx==-1? -1 : idx+1);
    }
}

void print_answers(int M,int *out){ for(int i=0;i<M;i++) printf("%d\n", out[i]); }

int main(void){ int N,M; long long *A=NULL,*B=NULL; read_input(&N,&M,&A,&B); int *out=(int*)malloc((size_t)M*sizeof(int)); process_all(N,M,A,B,out); print_answers(M,out); free(A); free(B); free(out); return 0; }
