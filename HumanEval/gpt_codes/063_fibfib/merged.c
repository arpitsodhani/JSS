#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int fibfib(int n) {
    if (n == 0) return 0;
    if (n == 1) return 0;
    if (n == 2) return 1;
    int a = 0, b = 0, c = 1;
    for (int i = 3; i <= n; i++) {
        int next = a + b + c;
        a = b; b = c; c = next;
    }
    return c;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", fibfib(n));
    return 0;
}

