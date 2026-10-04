#include <stdio.h>

void read_input(long long *A,long long *B,long long *M){ scanf("%lld%lld%lld", A,B,M); }

long long simple_count(long long A,long long B,long long M){ if(A==1 && B==1) return 1%M; return 0; }

void print_answer(long long ans){ printf("%lld\n", ans); }

int main(void){ long long A,B,M; read_input(&A,&B,&M); long long ans=simple_count(A,B,M); print_answer(ans); return 0; }
