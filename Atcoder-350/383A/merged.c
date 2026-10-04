#include <stdio.h>

void read_input(int *N,int *T,int *V){ scanf("%d", N); for(int i=0;i<*N;i++) scanf("%d%d", &T[i], &V[i]); }

int remaining(int N,int *T,int *V){
    int water=0;
    for(int i=0;i<N;i++){
        if(i==0) water = 0;
        else {
            int dt = T[i]-T[i-1];
            water -= dt;
            if(water<0) water=0;
        }
        water += V[i];
    }
    return water;
}

void print_answer(int w){ printf("%d\n", w); }

int main(void){ int N; static int T[105], V[105]; read_input(&N,T,V); int w=remaining(N,T,V); print_answer(w); return 0; }
