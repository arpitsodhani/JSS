#include <stdio.h>

int read_values(long long a[]) { int n; scanf("%d", &n); for(int i = 0; i < n; i++) scanf("%lld", &a[i]); return n; }

void sort_values(int n, long long a[]) { for(int i = 0; i < n - 1; i++) { for(int j = i + 1; j < n; j++) { if(a[i] > a[j]) { long long temp = a[i]; a[i] = a[j]; a[j] = temp; } } } }

long long compute_minimum_cost(int n, long long a[]) { long long cost = 0; for(int i = 0; i < n - 2; i++) cost += a[i]; cost += a[n - 2] * 2; cost += a[n - 1] * 2; return cost; }

int main() { long long a[100005]; int n = read_values(a); sort_values(n, a); printf("%lld\n", compute_minimum_cost(n, a)); return 0; }
