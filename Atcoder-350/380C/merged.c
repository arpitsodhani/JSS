#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_input(int *N,int *K,char *S){ scanf("%d%d", N,K); scanf("%s", S); }

int find_blocks(int N,char *S,int *L,int *R){
    int m=0;
    int i=0;
    while(i<N){
        if(S[i]=='1'){
            int l=i;
            while(i<N && S[i]=='1') i++;
            int r=i-1;
            L[m]=l; R[m]=r; m++;
        } else i++;
    }
    return m;
}

void move_k(int N,char *S,int *L,int *R,int K,char *T){
    int k=K-1;
    int l1=L[k-1], r1=R[k-1], l2=L[k], r2=R[k];
    for(int i=0;i<N;i++) T[i]=S[i];
    for(int i=r1+1;i<=r2;i++) T[i]='0';
    for(int i=0;i<=r1;i++) T[i]=S[i];
    int len=r2-l2+1;
    for(int i=0;i<len;i++) T[r1+1+i]='1';
    for(int i=r1+1+len;i<=r2;i++) T[i]='0';
}

void print_answer(char *T){ printf("%s\n", T); }

int main(void){ int N,K; char *S=(char*)malloc(600000); read_input(&N,&K,S); int *L=(int*)malloc((size_t)N*sizeof(int)); int *R=(int*)malloc((size_t)N*sizeof(int)); int m=find_blocks(N,S,L,R); char *T=(char*)malloc((size_t)N+1); T[N]=0; move_k(N,S,L,R,K,T); print_answer(T); free(S); free(L); free(R); free(T); return 0; }
