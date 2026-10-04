#include <stdio.h>

int compute(int l1, int r1, int l2, int r2) { return !(r1 <= l2 || r2 <= l1); }

int main() { int l[500000], r[500000]; int n = read_input(l, r); printf("%lld\n", count_pairs(l, r, n)); return 0; }

int read_input(int l[], int r[]) { int n; scanf("%d", &n); for(int i = 0; i < n; i++) scanf("%d%d", &l[i], &r[i]); return n; }

long long solve(int l[], int r[], int n) { long long cnt = 0; for(int i = 0; i < n - 1; i++) { for(int j = i + 1; j < n; j++) { if(intersects(l[i], r[i], l[j], r[j])) cnt++; } } return cnt; }

