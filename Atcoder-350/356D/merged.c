#include <stdio.h>

long long compute_sum(long long n, long long m) { const long long MOD = 998244353; long long sum = 0; for(int bit = 0; bit < 60; bit++) { if(!(m & (1LL << bit))) continue; long long cycle = 1LL << (bit + 1); long long full = (n + 1) / cycle; long long rem = (n + 1) % cycle; long long half = 1LL << bit; long long cnt = full * half + (rem > half ? rem - half : 0); sum = (sum + cnt) % MOD; } return sum; }

int count_bits(long long x) { int cnt = 0; while(x) { cnt += x & 1; x >>= 1; } return cnt; }

int main() { long long n, m; read_input(&n, &m); printf("%lld\n", compute_sum(n, m)); return 0; }

void read_input(long long *n, long long *m) { scanf("%lld%lld", n, m); }

