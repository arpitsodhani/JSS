#include <stdio.h>

void generate_even_digits(int a, int b, int* result, int* result_len) {
    int start = (a < b) ? a : b;
    int end = (a > b) ? a : b;
    
    *result_len = 0;
    for (int i = start; i <= end; i++) {
        if (i >= 2 && i <= 8 && i % 2 == 0) {
            result[(*result_len)++] = i;
        }
    }
}

int main() {
    int argument_count, a, b;
    scanf("%d %d %d", &argument_count, &a, &b);
    
    int result[100];
    int result_len;
    generate_even_digits(a, b, result, &result_len);
    
    for (int i = 0; i < result_len; i++) {
        if (i > 0) printf(" ");
        printf("%d", result[i]);
    }
    printf("\n");
    
    return 0;
}
