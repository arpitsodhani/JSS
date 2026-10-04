#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,long long *K,int **P){ scanf("%d%lld", N,K); *P=(int*)malloc((size_t)(*N)*sizeof(int)); for(int i=0;i<*N;i++) scanf("%d", &(*P)[i]); }

void build_jump(int N,int *P,int **jump){ int LOG=60; for(int i=0;i<LOG;i++) for(int j=0;j<N;j++) jump[i][j]=0; for(int j=0;j<N;j++) jump[0][j]=P[j]-1; for(int i=1;i<LOG;i++) for(int j=0;j<N;j++) jump[i][j]=jump[i-1][ jump[i-1][j] ]; }

void apply_jump(int N,long long K,int **jump,int *out){ int LOG=60; for(int i=0;i<N;i++){ int cur=i; for(int b=0;b<LOG;b++) if((K>>b)&1) cur=jump[b][cur]; out[i]=cur+1; } }

void print_answer(int N,int *out){ for(int i=0;i<N;i++){ if(i) putchar(' '); printf("%d", out[i]); } putchar('\n'); }

int main(void){ int N; long long K; int *P=NULL; read_input(&N,&K,&P); int LOG=60; int **jump=(int**)malloc((size_t)LOG*sizeof(int*)); for(int i=0;i<LOG;i++) jump[i]=(int*)malloc((size_t)N*sizeof(int)); build_jump(N,P,jump); int *out=(int*)malloc((size_t)N*sizeof(int)); apply_jump(N,K,jump,out); print_answer(N,out); for(int i=0;i<LOG;i++) free(jump[i]); free(jump); free(P); free(out); return 0; }
