#include <stdio.h>

int check_achievable(int n, long long stamina[], long long speed[], long long distance, long long max_stamina) { for(int i = 0; i < n; i++) { if(speed[i] == 0) continue; long long time_needed = (distance + speed[i] - 1) / speed[i]; long long cost = time_needed * stamina[i]; if(cost <= max_stamina) return 1; } return 0; }

int main() { long long a[105], b[105]; int n = read_styles(a, b); int q; scanf("%d", &q); process_queries(n, a, b, q); return 0; }

void process_queries(int n, long long stamina[], long long speed[], int q) { for(int i = 0; i < q; i++) { long long d, c; scanf("%lld%lld", &d, &c); printf("%s\n", check_achievable(n, stamina, speed, d, c) ? "Yes" : "No"); } }

int read_styles(long long stamina[], long long speed[]) { int n; scanf("%d", &n); for(int i = 0; i < n; i++) scanf("%lld%lld", &stamina[i], &speed[i]); return n; }

