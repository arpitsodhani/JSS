#include <stdio.h>

int sum_to_n(int n) {
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    return sum;
}

int main(void) {
    int n;
    scanf("%d", &n);
    int result = sum_to_n(n);
    printf("%d\n", result);
    return 0;
}
