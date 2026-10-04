#include <stdio.h>

void read_input(int *n, long long *c, int *m, int *t, long long *p) { scanf("%d%lld%d", n, c, m); for(int i = 0; i < *m; i++) scanf("%d%lld", &t[i], &p[i]); }

long long calc_cost(int from, int to, long long c) { return c * (from > to ? from - to : to - from); }

long long dp_solve(int n, long long c, int m, int *t, long long *p) { long long dp[200001]; for(int i = 0; i <= m; i++) dp[i] = -1e18; dp[0] = 0; int pos = 1; for(int i = 0; i < m; i++) { dp[i+1] = dp[i]; for(int j = 0; j <= i; j++) { long long cost = calc_cost(j == 0 ? 1 : t[j-1], t[i], c); long long gain = dp[j] + p[i] - cost; if(gain > dp[i+1]) dp[i+1] = gain; } } long long best = 0; for(int i = 0; i <= m; i++) if(dp[i] > best) best = dp[i]; return best; }

int main() { int n, m, t[200000]; long long c, p[200000]; read_input(&n, &c, &m, t, p); printf("%lld\n", dp_solve(n, c, m, t, p)); return 0; }
