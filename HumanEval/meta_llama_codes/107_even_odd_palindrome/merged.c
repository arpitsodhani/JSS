#include <stdio.h>

void count_even_odd_palindromes(int n, int *even_count, int *odd_count) {
    *even_count = 0;
    *odd_count = 0;
    for (int i = 1; i <= n; i++) {
        int num = i, rev = 0, temp = i;
        while (temp > 0) {
            rev = rev * 10 + temp % 10;
            temp /= 10;
        }
        if (num == rev) {
            if (i % 2 == 0) {
                (*even_count)++;
            } else {
                (*odd_count)++;
            }
        }
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    int even_count, odd_count;
    count_even_odd_palindromes(n, &even_count, &odd_count);
    printf("%d %d\n", even_count, odd_count);
    return 0;
}
