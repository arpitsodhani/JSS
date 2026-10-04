#include <stdio.h>

void read_input(int *A){ for(int i=0;i<4;i++) scanf("%d", &A[i]); }

int max_pairs(int *A){ int cnt[5]={0}; for(int i=0;i<4;i++) cnt[A[i]]++; int ans=0; for(int c=1;c<=4;c++) ans+=cnt[c]/2; return ans; }

void print_answer(int ans){ printf("%d\n", ans); }

int main(void){ int A[4]; read_input(A); int ans=max_pairs(A); print_answer(ans); return 0; }
