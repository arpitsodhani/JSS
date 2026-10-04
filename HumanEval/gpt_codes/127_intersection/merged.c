#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int is_prime(int n) {
    if (n < 2) return 0;
    if (n == 2) return 1;
    if (n % 2 == 0) return 0;
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) return 0;
    }
    return 1;
}

void intersection(int a1, int a2, int b1, int b2, char *result) {
    int start = (a1 > b1) ? a1 : b1;
    int end = (a2 < b2) ? a2 : b2;
    
    if (start > end) {
        strcpy(result, "NO");
        return;
    }
    
    int length = end - start;
    
    if (is_prime(length)) {
        strcpy(result, "YES");
    } else {
        strcpy(result, "NO");
    }
}

int main() {
    int a1, a2, b1, b2;
    scanf("%d %d %d %d", &a1, &a2, &b1, &b2);
    char result[10];
    intersection(a1, a2, b1, b2, result);
    printf("%s\n", result);
    return 0;
}
