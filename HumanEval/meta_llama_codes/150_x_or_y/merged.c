#include <stdio.h>

int is_prime(int n) {
    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main() {
    int n, x, y;
    scanf("%d %d %d", &n, &x, &y);
    
    if (is_prime(n)) {
        printf("%d\n", x);
    } else {
        printf("%d\n", y);
    }
    
    return 0;
}
