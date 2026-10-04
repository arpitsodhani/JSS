#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int validate_even_sum(int a, int b) {
    return (a + b) % 2 == 0;
}

int compute_midpoint(int a, int b) {
    return (a + b) / 2;
}

int determine_midpoint_existence(int a, int b, int *result) {
    if (validate_even_sum(a, b)) {
        *result = compute_midpoint(a, b);
        return 1;
    }
    return 0;
}

int main() {
    int a, b, result;
    scanf("%d %d", &a, &b);
    if (determine_midpoint_existence(a, b, &result)) {
        printf("%d\n", result);
    } else {
        printf("Impossible\n");
    }
    return 0;
}