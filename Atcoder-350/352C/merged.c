#include <stdio.h>

int read_input(long long *a, long long *b) { int n; scanf("%d", &n); for(int i = 0; i < n; i++) scanf("%lld%lld", &a[i], &b[i]); return n; }

long long compute_diff(long long a, long long b) { return b - a; }

void sort_by_diff(long long *a, long long *b, int n) { for(int i = 0; i < n - 1; i++) { for(int j = i + 1; j < n; j++) { if(compute_diff(a[i], b[i]) < compute_diff(a[j], b[j])) { long long tmp = a[i]; a[i] = a[j]; a[j] = tmp; tmp = b[i]; b[i] = b[j]; b[j] = tmp; } } } }

long long calc_height(long long *a, long long *b, int n) { long long h = 0; for(int i = 0; i < n; i++) { h += a[i]; } return h + b[n-1] - a[n-1]; }

int main() { long long a[200000], b[200000]; int n = read_input(a, b); sort_by_diff(a, b, n); printf("%lld\n", calc_height(a, b, n)); return 0; }
