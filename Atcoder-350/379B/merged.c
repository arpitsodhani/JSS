#include <stdio.h>
#include <string.h>

void read_input(int *N,int *K,char *S){ scanf("%d%d", N,K); scanf("%s", S); }

int max_strawberries(int N,int K,char *S){ int run=0,ans=0; for(int i=0;i<N;i++){ if(S[i]=='O') run++; else run=0; if(run==K){ ans++; run=0; } } return ans; }

void print_answer(int ans){ printf("%d\n", ans); }

int main(void){ int N,K; char S[205]; read_input(&N,&K,S); int ans=max_strawberries(N,K,S); print_answer(ans); return 0; }
