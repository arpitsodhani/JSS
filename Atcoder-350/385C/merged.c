#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,int **H){
    scanf("%d", N);
    *H = (int*)malloc((size_t)(*N)*sizeof(int));
    for(int i=0;i<*N;i++) scanf("%d", &(*H)[i]);
}

int max_buildings(int N,int *H){
    int best = 1;
    int *pos = (int*)malloc((size_t)N*sizeof(int));
    for(int h=1; h<=3000; h++){
        int k=0;
        for(int i=0;i<N;i++) if(H[i]==h) pos[k++]=i;
        if(k==0) continue;
        for(int i=0;i<k;i++){
            for(int j=i+1;j<k;j++){
                int d = pos[j]-pos[i];
                int cnt=2;
                int next = pos[j]+d;
                int idx=j+1;
                while(next<N){
                    while(idx<k && pos[idx]<next) idx++;
                    if(idx<k && pos[idx]==next){ cnt++; next+=d; idx++; }
                    else break;
                }
                if(cnt>best) best=cnt;
            }
        }
        if(best<1) best=1;
    }
    free(pos);
    return best;
}

void print_answer(int ans){ printf("%d\n", ans); }

int main(void){
    int N; int *H=NULL;
    read_input(&N,&H);
    int ans = max_buildings(N,H);
    print_answer(ans);
    free(H);
    return 0;
}
