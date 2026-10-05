#include <stdio.h>

long long compute_special_factorial(int n) {
    long long result = 1;
    for (int i = 1; i <= n; i++) {
        long long fact = 1;
        for (int j = 1; j <= i; j++) {
            fact *= j;
        }
        result *= fact;
    }
    return result;
}

int main() {
    int n;
    scanf("%d", &n);
    
    printf("%lld\n", compute_special_factorial(n));
    return 0;
}
