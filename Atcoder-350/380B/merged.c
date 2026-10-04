#include <stdio.h>
#include <string.h>

void read_input(char *S){ scanf("%s", S); }

int parse_counts(char *S,int *out){
    int n=strlen(S);
    int idx=0, cur=0;
    for(int i=1;i<n;i++){
        if(S[i]=='-') cur++;
        else { out[idx++]=cur; cur=0; }
    }
    return idx;
}

void print_answer(int n,int *out){ for(int i=0;i<n;i++){ if(i) putchar(' '); printf("%d", out[i]); } putchar('\n'); }

int main(void){ char S[205]; read_input(S); int out[200]; int n=parse_counts(S,out); print_answer(n,out); return 0; }
