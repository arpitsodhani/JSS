#include <stdio.h>

void read_input(int *N,int *D,char *S){ scanf("%d%d", N,D); scanf("%s", S); }

int count_empty(int N,int D,char *S){
    int dots=0;
    for(int i=0;i<N;i++) if(S[i]=='.') dots++;
    return dots + D;
}

void print_answer(int ans){ printf("%d\n", ans); }

int main(void){ int N,D; char S[205]; read_input(&N,&D,S); int ans=count_empty(N,D,S); print_answer(ans); return 0; }
