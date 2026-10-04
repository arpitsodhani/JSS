#include <stdio.h>

void read_input(int *n, long long *a) {
scanf("%d", n); for(int i=0;i<*n;i++) scanf("%lld", &a[i]);
}

int longest_run(int n, const long long *a) {
int best=1,cur=1; for(int i=1;i<n;i++){ if(a[i]==a[i-1]) cur++; else cur=1; if(cur>best) best=cur; } return best;
}

void print_ans(int x) {
printf("%d\n", x);
}

int main(void){ int n; static long long a[200005]; read_input(&n,a); int ans=longest_run(n,a); print_ans(ans); return 0; }
