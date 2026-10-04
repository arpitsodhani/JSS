#include <stdio.h>

int read_n(void) {
int n; scanf("%d", &n); return n;
}

int max_value(int n) {
int best=0; for(int i=0;i<n;i++){ int x; scanf("%d", &x); if(x>best) best=x; } return best;
}

void print_int(int x) {
printf("%d\n", x);
}

int main(void){ int n=read_n(); int ans=max_value(n); print_int(ans); return 0; }
