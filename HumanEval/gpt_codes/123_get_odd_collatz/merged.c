#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int compare_int(const void *a, const void *b) {
    return *(int*)a - *(int*)b;
}

void get_odd_collatz(int n, int *result, int *size) {
    *size = 0;
    int seen[1000] = {0};
    
    while (n != 1) {
        if (n % 2 == 1 && !seen[*size]) {
            result[*size] = n;
            seen[*size] = 1;
            (*size)++;
        }
        if (n % 2 == 0) {
            n = n / 2;
        } else {
            n = 3 * n + 1;
        }
    }
    
    qsort(result, *size, sizeof(int), compare_int);
}

int main() {
    int n;
    scanf("%d", &n);
    int result[1000], size;
    get_odd_collatz(n, result, &size);
    for (int i = 0; i < size; i++) {
        printf("%d", result[i]);
        if (i < size - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
