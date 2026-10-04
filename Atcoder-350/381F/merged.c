#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int **A){ scanf("%d", N); *A=(int*)malloc((size_t)(*N)*sizeof(int)); for(int i=0;i<*N;i++) scanf("%d", &(*A)[i]); }

int build_subseq(int *A,int N,int mask,int *vals){ int len=0; for(int i=0;i<N;i++) if(mask>>i & 1) vals[len++]=A[i]; return len; }

int check_pairs(int *vals,int len){ if(len%2) return 0; for(int i=0;i<len;i+=2) if(vals[i]!=vals[i+1]) return 0; return 1; }

int check_unique(int *vals,int len){ for(int i=0;i<len;i+=2){ for(int j=i+2;j<len;j+=2) if(vals[i]==vals[j]) return 0; } return 1; }

int is_1122_subseq(int *A,int N,int mask){
    int vals[40];
    int len=build_subseq(A,N,mask,vals);
    if(!check_pairs(vals,len)) return 0;
    if(!check_unique(vals,len)) return 0;
    return 1;
}

int max_len(int N,int *A){
    int best=0;
    int total=1<<N;
    for(int mask=0; mask<total; mask++){
        int len=0;
        for(int i=0;i<N;i++) if(mask>>i & 1) len++;
        if(len<=best || len%2) continue;
        if(is_1122_subseq(A,N,mask)) best=len;
    }
    return best;
}

void print_answer(int ans){ printf("%d\n", ans); }

int main(void){ int N; int *A=NULL; read_input(&N,&A); int ans=max_len(N,A); print_answer(ans); free(A); return 0; }
