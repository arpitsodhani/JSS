#include <stdio.h>

void factorize(int n, int *factors, int *count) {
    *count = 0;
    for (int i = 2; i * i <= n; i++) {
        while (n % i == 0) {
            factors[(*count)++] = i;
            n /= i;
        }
    }
    if (n > 1) {
        factors[(*count)++] = n;
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    int factors[1000];
    int count;
    factorize(n, factors, &count);
    for (int i = 0; i < count; i++) {
        printf("%d", factors[i]);
        if (i < count - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
