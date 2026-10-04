#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_input(int *N,char *S){ scanf("%d", N); scanf("%s", S); }

void build_runs(int N,char *S,int *L1,int *R2){
    for(int i=0;i<N;i++){
        if(S[i]=='1') L1[i]=(i?L1[i-1]:0)+1; else L1[i]=0;
    }
    for(int i=N-1;i>=0;i--){
        if(S[i]=='2') R2[i]=(i+1<N?R2[i+1]:0)+1; else R2[i]=0;
    }
}

int max_substring(int N,char *S,int *L1,int *R2){
    int best=0;
    for(int i=0;i<N;i++){
        if(S[i]!='/') continue;
        int l = (i>0? L1[i-1]:0);
        int r = (i+1<N? R2[i+1]:0);
        int k = l<r?l:r;
        int len = 2*k+1;
        if(len>best) best=len;
    }
    return best;
}

void print_answer(int ans){ printf("%d\n", ans); }

int main(void){ int N; char *S=(char*)malloc(300000); read_input(&N,S); int *L1=(int*)malloc((size_t)N*sizeof(int)); int *R2=(int*)malloc((size_t)N*sizeof(int)); build_runs(N,S,L1,R2); int ans=max_substring(N,S,L1,R2); print_answer(ans); free(S); free(L1); free(R2); return 0; }
