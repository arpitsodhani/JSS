#include <stdio.h>

int read_input(long long *a) { int n; scanf("%d", &n); for(int i = 0; i < n; i++) scanf("%lld", &a[i]); return n; }

int count_digits(long long x) { int cnt = 0; while(x > 0) { cnt++; x /= 10; } return cnt; }

long long concat_numbers(long long x, long long y) { int d = count_digits(y); long long mul = 1; for(int i = 0; i < d; i++) mul *= 10; return (x * mul + y) % 998244353LL; }

long long sum_pairs(long long *a, int n) { long long res = 0; for(int i = 0; i < n - 1; i++) { for(int j = i + 1; j < n; j++) { res = (res + concat_numbers(a[i], a[j])) % 998244353LL; } } return res; }

int main() { long long a[200000]; int n = read_input(a); printf("%lld\n", sum_pairs(a, n)); return 0; }
