#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void read_limit(long long *n) {
    scanf("%lld", n);
}

long long count_perfect_powers(long long n) {
    int marked[100000] = {0};
    int count = 0;
    for (long long b = 2; b <= 60; b++) {
        long long max_a = (long long)pow(n, 1.0 / b);
        for (long long a = 2; a <= max_a + 1; a++) {
            long long val = 1;
            int overflow = 0;
            for (int i = 0; i < b; i++) {
                if (val > n / a) {
                    overflow = 1;
                    break;
                }
                val *= a;
            }
            if (!overflow && val <= n) {
                if (val < 100000) {
                    if (!marked[val]) {
                        marked[val] = 1;
                        count++;
                    }
                }
            }
        }
    }
    return count;
}

int main() {
    long long n;
    read_limit(&n);
    printf("%lld\n", count_perfect_powers(n));
    return 0;
}

