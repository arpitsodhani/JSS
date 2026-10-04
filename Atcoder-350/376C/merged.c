#include <stdio.h>
#include <stdlib.h>

void read_input(int *N,long long **A){ scanf("%d", N); *A=(long long*)malloc((size_t)(*N)*sizeof(long long)); for(int i=0;i<*N;i++) scanf("%lld", &(*A)[i]); }

void sort_sizes(int N,long long *A){ for(int i=0;i<N;i++) for(int j=i+1;j<N;j++) if(A[j]<A[i]){ long long t=A[i]; A[i]=A[j]; A[j]=t; } }

int min_boxes(int N,long long *A){ int boxes=0; long long cur=0; for(int i=0;i<N;i++){ if(cur<A[i]){ boxes++; cur=A[i]; } cur++; } return boxes; }

void print_answer(int ans){ printf("%d\n", ans); }

int main(void){ int N; long long *A=NULL; read_input(&N,&A); sort_sizes(N,A); int ans=min_boxes(N,A); print_answer(ans); free(A); return 0; }
