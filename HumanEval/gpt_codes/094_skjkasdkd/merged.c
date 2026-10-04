#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int is_prime(int n) {
    if (n < 2) return 0;
    if (n == 2) return 1;
    if (n % 2 == 0) return 0;
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int find_largest_prime(int n, int lst[]) {
    int max_prime = -1;
    for (int i = 0; i < n; i++) {
        if (is_prime(lst[i]) && lst[i] > max_prime) {
            max_prime = lst[i];
        }
    }
    return max_prime;
}

int digit_sum(int n) {
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

void run(void) {

    int n;
    scanf("%d", &n);
    int lst[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &lst[i]);
    }
    int largest_prime = find_largest_prime(n, lst);
    printf("%d\n", largest_prime == -1 ? 0 : digit_sum(largest_prime));
}

int main() {
    run();
    return 0;
}
