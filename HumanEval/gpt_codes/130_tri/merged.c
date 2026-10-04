#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

void tri(int n, int *result) {
    result[0] = 1;
    if (n == 0) return;
    
    result[1] = 3;
    if (n == 1) return;
    
    for (int i = 2; i <= n; i++) {
        if (i % 2 == 0) {
            result[i] = 1 + i / 2;
        } else {
            result[i] = result[i - 1] + result[i - 2] + (i + 3) / 2;
        }
    }
}

int main() {
    int n;
    scanf("%d", &n);
    int result[n + 1];
    tri(n, result);
    for (int i = 0; i <= n; i++) {
        printf("%d", result[i]);
        if (i < n) printf(" ");
    }
    printf("\n");
    return 0;
}
