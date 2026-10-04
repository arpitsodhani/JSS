#include <stdio.h>

void read_input(int *N,int *R,int *D,int *A){ scanf("%d%d", N,R); for(int i=0;i<*N;i++) scanf("%d%d", &D[i], &A[i]); }

int final_rating(int N,int R,int *D,int *A){
    int r=R;
    for(int i=0;i<N;i++){
        if(D[i]==1){
            if(r>=1600 && r<=2799) r += A[i];
        } else {
            if(r>=1200 && r<=2399) r += A[i];
        }
    }
    return r;
}

void print_answer(int r){ printf("%d\n", r); }

int main(void){
    int N,R; static int D[105], A[105];
    read_input(&N,&R,D,A);
    int r = final_rating(N,R,D,A);
    print_answer(r);
    return 0;
}
