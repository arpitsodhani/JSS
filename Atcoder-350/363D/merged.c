#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_n(long long *n) {
    scanf("%lld", n);
}

long long compute_nth_palindrome(long long n) {
    if (n <= 9) return n;
    n -= 9;
    for (int len = 2; ; len++) {
        int half = (len + 1) / 2;
        long long count = 9;
        for (int i = 1; i < half; i++) count *= 10;
        if (n <= count) {
            long long base = 1;
            for (int i = 1; i < half; i++) base *= 10;
            long long num = base + n - 1;
            char s[25];
            sprintf(s, "%lld", num);
            int slen = strlen(s);
            for (int i = len - slen; i < len; i++) s[i] = s[len - 1 - i];
            s[len] = '\0';
            long long result = 0;
            for (int i = 0; i < len; i++) result = result * 10 + (s[i] - '0');
            return result;
        }
        n -= count;
    }
}

int main() {
    long long n;
    read_n(&n);
    printf("%lld\n", compute_nth_palindrome(n));
    return 0;
}
