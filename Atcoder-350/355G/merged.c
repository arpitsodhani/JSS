#include <stdio.h>

long long compute(int pos, int chosen[], int k) { long long min_dist = 1000000000; for(int i = 0; i < k; i++) { long long d = pos > chosen[i] ? pos - chosen[i] : chosen[i] - pos; if(d < min_dist) min_dist = d; } return min_dist; }

int main() { int k; long long p[50000]; int n = read_input(&k, p); printf("%lld\n", solve(p, n, k)); return 0; }

long long process(int chosen[], int k, long long p[], int n) { long long sum = 0; for(int y = 0; y < n; y++) { long long dist = compute(y, chosen, k); sum += dist * p[y]; } return sum; }

int read_input(int *k, long long p[]) { int n; scanf("%d%d", &n, k); for(int i = 0; i < n; i++) scanf("%lld", &p[i]); return n; }

long long solve(long long p[], int n, int k) { long long best = 9999999999999LL; int x[100]; for(int mask = 0; mask < (1 << n); mask++) { int cnt = 0; for(int i = 0; i < n; i++) if(mask & (1 << i)) x[cnt++] = i; if(cnt != k) continue; long long val = process(x, k, p, n); if(val < best) best = val; } return best; }

