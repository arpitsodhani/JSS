#include <stdio.h>
#include <stdlib.h>

void read_input(int *H,int *W,int *N,int **R,int **C,int **L){ scanf("%d%d%d", H,W,N); *R=(int*)malloc((size_t)(*N)*sizeof(int)); *C=(int*)malloc((size_t)(*N)*sizeof(int)); *L=(int*)malloc((size_t)(*N)*sizeof(int)); for(int i=0;i<*N;i++) scanf("%d%d%d", &(*R)[i], &(*C)[i], &(*L)[i]); }

void simulate(int H,int W,int N,int *R,int *C,int *L,int *out){
    int total_cells=0;
    for(int i=0;i<N;i++) total_cells += L[i];
    long long *cells=(long long*)malloc((size_t)total_cells*sizeof(long long));
    int *start=(int*)malloc((size_t)N*sizeof(int));
    int idx=0;
    for(int i=0;i<N;i++){
        start[i]=idx;
        for(int k=0;k<L[i];k++) cells[idx++]=(long long)(R[i])*1000000LL + (C[i]+k);
    }
    int moved=1;
    for(int step=0; step<H && moved; step++){
        moved=0;
        for(int i=0;i<N;i++){
            int can=1;
            for(int k=0;k<L[i];k++){
                long long v=cells[start[i]+k];
                int r=(int)(v/1000000LL);
                int c=(int)(v%1000000LL);
                if(r>=H) { can=0; break; }
                for(int j=0;j<total_cells;j++){
                    if(j>=start[i] && j<start[i]+L[i]) continue;
                    if(cells[j]==(long long)(r+1)*1000000LL + c){ can=0; break; }
                }
                if(!can) break;
            }
            if(can){
                moved=1;
                for(int k=0;k<L[i];k++) cells[start[i]+k]+=1000000LL;
            }
        }
    }
    for(int i=0;i<N;i++){
        long long v=cells[start[i]];
        out[i]=(int)(v/1000000LL);
    }
    free(cells); free(start);
}

void print_answer(int N,int *out){ for(int i=0;i<N;i++) printf("%d\n", out[i]); }

int main(void){ int H,W,N; int *R=NULL,*C=NULL,*L=NULL; read_input(&H,&W,&N,&R,&C,&L); int *out=(int*)malloc((size_t)N*sizeof(int)); simulate(H,W,N,R,C,L,out); print_answer(N,out); free(R); free(C); free(L); free(out); return 0; }
