#include <stdio.h>

long long read_number() { long long n; scanf("%lld", &n); return n; }

int count_digits(long long n) { int d = 0; long long temp = n; while(temp > 0) { d++; temp /= 10; } return d; }

long long compute_power_mod(long long base, long long exp, long long mod) { long long result = 1; base %= mod; while(exp > 0) { if(exp % 2 == 1) result = (result * base) % mod; base = (base * base) % mod; exp /= 2; } return result; }

long long calculate_concatenation_value(long long n) { const long long MOD = 998244353; int digits = count_digits(n); long long power = compute_power_mod(10, (long long)digits * n, MOD); long long numerator = (n % MOD) * ((power - 1 + MOD) % MOD) % MOD; long long denom_inv = compute_power_mod(compute_power_mod(10, digits, MOD) - 1 + MOD, MOD - 2, MOD); return (numerator * denom_inv) % MOD; }

int main() { long long n = read_number(); printf("%lld\n", calculate_concatenation_value(n)); return 0; }
