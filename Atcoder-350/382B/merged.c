#include <stdio.h>
#include <string.h>

void read_input(int *N,int *D,char *S){ scanf("%d%d", N,D); scanf("%s", S); }

void eat_rightmost(int N,int D,char *S){
    for(int k=0;k<D;k++){
        for(int i=N-1;i>=0;i--){
            if(S[i]=='@'){ S[i]='.'; break; }
        }
    }
}

void print_answer(char *S){ printf("%s\n", S); }

int main(void){ int N,D; char S[205]; read_input(&N,&D,S); eat_rightmost(N,D,S); print_answer(S); return 0; }
