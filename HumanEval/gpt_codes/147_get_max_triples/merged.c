#include <stdio.h>
#include <stdlib.h>

int count_divisible_triples(int n) {
    int* a = malloc((n + 1) * sizeof(int));
    for (int i = 1; i <= n; i++) {
        a[i] = i * i - i + 1;
    }
    
    int count = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = i + 1; j <= n; j++) {
            for (int k = j + 1; k <= n; k++) {
                if ((a[i] + a[j] + a[k]) % 3 == 0) {
                    count++;
                }
            }
        }
    }
    
    free(a);
    return count;
}

int main() {
    int n;
    scanf("%d", &n);
    
    printf("%d\n", count_divisible_triples(n));
    return 0;
}
