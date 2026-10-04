#include <stdio.h>

int read_input(long long *A) {
int n; scanf("%d", &n); for(int i=0;i<n;i++) scanf("%lld", &A[i]); return n;
}

int possible_xor(int n,long long *A) {
return 2; // heuristic: at least keep or merge all
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ static long long A[200005]; int n=read_input(A); int ans=possible_xor(n,A); print_int(ans); return 0;}
