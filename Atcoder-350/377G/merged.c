#include <stdio.h>
#include <string.h>

void read_input(int *N,char S[][100005]){ scanf("%d", N); for(int i=0;i<*N;i++) scanf("%s", S[i]); }

int lcp(char *a,char *b){ int i=0; while(a[i] && b[i] && a[i]==b[i]) i++; return i; }

int cost_to(char *s,char *t){ int l=lcp(s,t); int ls=strlen(s), lt=strlen(t); return (ls-l)+(lt-l); }

void solve_all(int N,char S[][100005],int *out){
    for(int k=0;k<N;k++){
        int best=strlen(S[k]);
        for(int j=0;j<k;j++){
            int c=cost_to(S[k],S[j]);
            if(c<best) best=c;
        }
        out[k]=best;
    }
}

void print_answer(int N,int *out){ for(int i=0;i<N;i++) printf("%d\n", out[i]); }

int main(void){ int N; static char S[65][100005]; read_input(&N,S); int out[65]; solve_all(N,S,out); print_answer(N,out); return 0; }
