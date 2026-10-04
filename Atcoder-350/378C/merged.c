#include <stdio.h>

void read_input(int *N,int *A){ scanf("%d", N); for(int i=0;i<*N;i++) scanf("%d", &A[i]); }

void last_positions(int N,int *A,int *out){ static int last[200005]; for(int i=0;i<=200000;i++) last[i]=-1; for(int i=0;i<N;i++){ out[i]=last[A[i]]; last[A[i]]=i+1; } }

void print_answer(int N,int *out){ for(int i=0;i<N;i++) printf("%d\n", out[i]); }

int main(void){ int N; static int A[200005], out[200005]; read_input(&N,A); last_positions(N,A,out); print_answer(N,out); return 0; }
