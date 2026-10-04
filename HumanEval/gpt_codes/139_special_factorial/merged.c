#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

long long special_factorial(int n) {
    long long result = 1;
    long long factorial = 1;
    
    for (int i = 1; i <= n; i++) {
        factorial *= i;
        result *= factorial;
    }
    
    return result;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%lld\n", special_factorial(n));
    return 0;
}
