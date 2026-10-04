#include <stdio.h>

int is_prime(int n) {
    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main() {
    int n;
    scanf("%d", &n);
    
    int a = 0, b = 1;
    int count = 0;
    
    while (count < n) {
        int next = a + b;
        if (is_prime(next)) {
            count++;
            if (count == n) {
                printf("%d\n", next);
                return 0;
            }
        }
        a = b;
        b = next;
    }
    
    return 0;
}
