#include <stdio.h>
#include <string.h>

void read_input(char *S,int *Q,long long *K){ scanf("%s", S); scanf("%d", Q); for(int i=0;i<*Q;i++) scanf("%lld", &K[i]); }

char resolve_char(char *S,long long k){
    long long n=strlen(S);
    long long L=n;
    while(L<k) L*=2;
    int flip=0;
    while(L>n){
        long long half=L/2;
        if(k>half){ k-=half; flip^=1; }
        L=half;
    }
    char c=S[k-1];
    if(flip){
        if(c>='a' && c<='z') c = c-'a'+'A';
        else if(c>='A' && c<='Z') c = c-'A'+'a';
    }
    return c;
}

void process_queries(char *S,int Q,long long *K,char *out){ for(int i=0;i<Q;i++) out[i]=resolve_char(S,K[i]); }

void print_answers(int Q,char *out){ for(int i=0;i<Q;i++) printf("%c\n", out[i]); }

int main(void){ char S[300000]; int Q; long long *K=(long long*)malloc((size_t)200000*sizeof(long long)); read_input(S,&Q,K); char *out=(char*)malloc((size_t)Q); process_queries(S,Q,K,out); print_answers(Q,out); free(K); free(out); return 0; }
