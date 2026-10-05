#include <stdio.h>

void get_odd_collatz_numbers(int n, int* result, int* result_len) {
    *result_len = 0;
    result[(*result_len)++] = n;
    
    while (n != 1) {
        if (n % 2 == 0) {
            n = n / 2;
        } else {
            n = 3 * n + 1;
        }
        
        if (n % 2 == 1) {
            int found = 0;
            for (int i = 0; i < *result_len; i++) {
                if (result[i] == n) {
                    found = 1;
                    break;
                }
            }
            if (!found) {
                result[(*result_len)++] = n;
            }
        }
    }
    
    // Sort
    for (int i = 0; i < *result_len - 1; i++) {
        for (int j = i + 1; j < *result_len; j++) {
            if (result[i] > result[j]) {
                int tmp = result[i];
                result[i] = result[j];
                result[j] = tmp;
            }
        }
    }
}

int main() {
    int n;
    scanf("%d", &n);
    
    int result[10000];
    int result_len;
    get_odd_collatz_numbers(n, result, &result_len);
    
    printf("[");
    for (int i = 0; i < result_len; i++) {
        if (i > 0) printf(", ");
        printf("%d", result[i]);
    }
    printf("]\n");
    
    return 0;
}
