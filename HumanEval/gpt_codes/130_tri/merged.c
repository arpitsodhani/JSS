#include <stdio.h>

void compute_tri(int n, int* result) {
    if (n >= 0) result[0] = 1;
    if (n >= 1) result[1] = 3;
    
    for (int i = 2; i <= n; i++) {
        if (i % 2 == 0) {
            result[i] = 1 + i / 2;
        } else {
            result[i] = result[i - 1] + result[i - 2] + 1 + (i + 1) / 2;
        }
    }
}

int main() {
    int n;
    scanf("%d", &n);
    
    int result[1000];
    compute_tri(n, result);
    
    for (int i = 0; i <= n; i++) {
        if (i > 0) printf(" ");
        printf("%d", result[i]);
    }
    printf("\n");
    
    return 0;
}
