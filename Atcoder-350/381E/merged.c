#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_input(int *N,int *Q,char *S,int **L,int **R){ scanf("%d%d", N,Q); scanf("%s", S); *L=(int*)malloc((size_t)(*Q)*sizeof(int)); *R=(int*)malloc((size_t)(*Q)*sizeof(int)); for(int i=0;i<*Q;i++) scanf("%d%d", &(*L)[i], &(*R)[i]); }

int count_left(char *S,int l,int i){ int c=0; for(int j=i-1;j>=l;j--) if(S[j]=='1') c++; return c; }

int count_right(char *S,int i,int r){ int c=0; for(int j=i+1;j<=r;j++) if(S[j]=='2') c++; return c; }

int best_for_slash(char *S,int l,int r,int i){ int c1=count_left(S,l,i); int c2=count_right(S,i,r); int k=c1<c2?c1:c2; return 2*k+1; }

int best_subseq(char *S,int l,int r){
    int best=0;
    for(int i=l;i<=r;i++){
        if(S[i]!='/') continue;
        int len=best_for_slash(S,l,r,i);
        if(len>best) best=len;
    }
    return best;
}

void process_queries(int Q,char *S,int *L,int *R,int *out){ for(int i=0;i<Q;i++){ out[i]=best_subseq(S,L[i]-1,R[i]-1); } }

void print_answers(int Q,int *out){ for(int i=0;i<Q;i++) printf("%d\n", out[i]); }

int main(void){ int N,Q; char *S=(char*)malloc(300000); int *L=NULL,*R=NULL; read_input(&N,&Q,S,&L,&R); int *out=(int*)malloc((size_t)Q*sizeof(int)); process_queries(Q,S,L,R,out); print_answers(Q,out); free(S); free(L); free(R); free(out); return 0; }
