#include <stdio.h>

int read_arrays(long long a[], long long b[]) { int n; scanf("%d", &n); for(int i = 1; i <= n; i++) scanf("%lld", &a[i]); for(int i = 1; i <= n; i++) scanf("%lld", &b[i]); return n; }

void apply_range_update_a(long long a[], int l, int r, long long x) { for(int i = l; i <= r; i++) a[i] += x; }

void apply_range_update_b(long long b[], int l, int r, long long x) { for(int i = l; i <= r; i++) b[i] += x; }

long long compute_product_sum(long long a[], long long b[], int l, int r) { const long long MOD = 998244353; long long sum = 0; for(int i = l; i <= r; i++) { sum = (sum + (a[i] % MOD) * (b[i] % MOD)) % MOD; } return sum; }

void process_queries(int n, long long a[], long long b[], int q) { for(int i = 0; i < q; i++) { int type; scanf("%d", &type); if(type == 1) { int l, r; long long x; scanf("%d%d%lld", &l, &r, &x); apply_range_update_a(a, l, r, x); } else if(type == 2) { int l, r; long long x; scanf("%d%d%lld", &l, &r, &x); apply_range_update_b(b, l, r, x); } else { int l, r; scanf("%d%d", &l, &r); printf("%lld\n", compute_product_sum(a, b, l, r)); } } }

int main() { long long a[200005], b[200005]; int n = read_arrays(a, b); int q; scanf("%d", &q); process_queries(n, a, b, q); return 0; }
