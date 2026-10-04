#include <stdio.h>

int read_input(int *a) { int n; scanf("%d", &n); for(int i = 0; i < n; i++) scanf("%d", &a[i]); return n; }

long long mod_inv(long long x) { long long res = 1, p = 998244353 - 2, base = x, mod = 998244353; while(p) { if(p & 1) res = (res * base) % mod; base = (base * base) % mod; p >>= 1; } return res; }

long long calc_expected(int *a, int n) { long long total = 0; for(int i = 0; i < n; i++) total += a[i]; long long sum = 0, mod = 998244353; for(int i = 0; i < n; i++) { long long contrib = (total + 1) % mod; contrib = (contrib * mod_inv(a[i])) % mod; sum = (sum + contrib) % mod; total -= a[i]; } return sum; }

int main() { int a[300000]; int n = read_input(a); printf("%lld\n", calc_expected(a, n)); return 0; }
