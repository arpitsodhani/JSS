#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int *M){ scanf("%d%d", N,M); }

void dfs(int idx,int N,int M,int *A,int last){
    if(idx==N){
        for(int i=0;i<N;i++){ if(i) putchar(' '); printf("%d", A[i]); }
        putchar('\n');
        return;
    }
    int start = (idx==0? 1 : last+10);
    for(int x=start; x<=M; x++){
        A[idx]=x;
        dfs(idx+1,N,M,A,x);
    }
}

void generate_all(int N,int M){ int *A=(int*)malloc((size_t)N*sizeof(int)); dfs(0,N,M,A,0); free(A); }

int main(void){ int N,M; read_input(&N,&M); generate_all(N,M); return 0; }
