#include <stdio.h>

void read_counts(int counts[]) { for(int i = 0; i < 26; i++) scanf("%d", &counts[i]); }

long long compute_factorial(int n, long long mod) { long long result = 1; for(int i = 1; i <= n; i++) result = (result * i) % mod; return result; }

long long power_mod(long long base, long long exp, long long mod) { long long result = 1; base %= mod; while(exp > 0) { if(exp & 1) result = (result * base) % mod; base = (base * base) % mod; exp >>= 1; } return result; }

long long count_arrangements(int counts[]) { long long MOD = 998244353; int total = 0; for(int i = 0; i < 26; i++) total += counts[i]; long long numerator = compute_factorial(total - 1, MOD); long long denominator = 1; for(int i = 0; i < 26; i++) { if(counts[i] > 0) { long long fact = compute_factorial(counts[i], MOD); denominator = (denominator * fact) % MOD; } } long long inv = power_mod(denominator, MOD - 2, MOD); return (numerator * inv) % MOD; }

int main() { int counts[26]; read_counts(counts); printf("%lld\n", count_arrangements(counts)); return 0; }
