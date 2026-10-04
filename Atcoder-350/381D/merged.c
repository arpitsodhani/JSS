#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int **A){ scanf("%d", N); *A=(int*)malloc((size_t)(*N)*sizeof(int)); for(int i=0;i<*N;i++) scanf("%d", &(*A)[i]); }

int longest_1122(int N,int *A){
    int best=0;
    int maxV=200000;
    int *last=(int*)malloc((size_t)(maxV+1)*sizeof(int));
    for(int i=0;i<=maxV;i++) last[i]=-1;
    for(int parity=0; parity<2; parity++){
        int l=parity, r=parity;
        for(int i=parity; i+1<N; i+=2){
            if(A[i]!=A[i+1]){
                l=i+2;
                for(int t=0;t<=maxV;t++) last[t]=-1;
                continue;
            }
            int val=A[i];
            if(last[val]>=l){
                l=last[val]+2;
            }
            last[val]=i;
            int len=i-l+2;
            if(len>best) best=len;
        }
        for(int i=0;i<=maxV;i++) last[i]=-1;
    }
    free(last);
    return best;
}

void print_answer(int ans){ printf("%d\n", ans); }

int main(void){ int N; int *A=NULL; read_input(&N,&A); int ans=longest_1122(N,A); print_answer(ans); free(A); return 0; }
