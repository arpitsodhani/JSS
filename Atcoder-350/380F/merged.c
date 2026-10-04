#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int *M,int *L,int **A,int **B,int **C){ scanf("%d%d%d", N,M,L); *A=(int*)malloc((size_t)(*N)*sizeof(int)); *B=(int*)malloc((size_t)(*M)*sizeof(int)); *C=(int*)malloc((size_t)(*L)*sizeof(int)); for(int i=0;i<*N;i++) scanf("%d", &(*A)[i]); for(int i=0;i<*M;i++) scanf("%d", &(*B)[i]); for(int i=0;i<*L;i++) scanf("%d", &(*C)[i]); }

int make_value_array(int N,int M,int L,int *A,int *B,int *C,int *val){ int idx=0; for(int i=0;i<N;i++) val[idx++]=A[i]; for(int i=0;i<M;i++) val[idx++]=B[i]; for(int i=0;i<L;i++) val[idx++]=C[i]; return idx; }

int count_bits(int mask,int total){ int c=0; for(int i=0;i<total;i++) if(mask>>i &1) c++; return c; }

int solve(int maskA,int maskB,int total,int *val){
    static int memo[1<<20];
    static char vis[1<<20];
    int key = (maskA<<10) ^ maskB;
    if(vis[key]) return memo[key];
    vis[key]=1;
    int win=0;
    // current player is A if depth even (maskA^maskB parity)
    int cntA=count_bits(maskA,total), cntB=count_bits(maskB,total);
    int turnA = ( (cntA+cntB)%2==0 );
    int maskT = ((1<<total)-1) & (~maskA) & (~maskB);
    int cur = turnA? maskA: maskB;
    for(int i=0;i<total;i++){
        if(cur>>i &1){
            int newMaskA=maskA, newMaskB=maskB;
            if(turnA) newMaskA &= ~(1<<i); else newMaskB &= ~(1<<i);
            int best=0;
            // option: take none
            if(!solve(newMaskA, newMaskB, total, val)) best=1;
            // option: take one lower table card
            for(int j=0;j<total && !best;j++){
                if(maskT>>j &1){
                    if(val[j] < val[i]){
                        int nmA=newMaskA, nmB=newMaskB;
                        if(turnA) nmA |= (1<<j); else nmB |= (1<<j);
                        if(!solve(nmA,nmB,total,val)) best=1;
                    }
                }
            }
            if(best){ win=1; break; }
        }
    }
    memo[key]=win;
    return win;
}

int determine_winner(int N,int M,int L,int *A,int *B,int *C){ int total=N+M+L; int *val=(int*)malloc((size_t)total*sizeof(int)); make_value_array(N,M,L,A,B,C,val); int maskA=0,maskB=0; for(int i=0;i<N;i++) maskA |= (1<<i); for(int i=0;i<M;i++) maskB |= (1<<(N+i)); int win=solve(maskA,maskB,total,val); free(val); return win; }

void print_answer(int win){ printf("%s\n", win?"Takahashi":"Aoki"); }

int main(void){ int N,M,L; int *A=NULL,*B=NULL,*C=NULL; read_input(&N,&M,&L,&A,&B,&C); int win=determine_winner(N,M,L,A,B,C); print_answer(win); free(A); free(B); free(C); return 0; }
