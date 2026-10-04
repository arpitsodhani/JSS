#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int is_equal_to_sum_even(int n) {
    return n >= 8 && n % 2 == 0;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%s\n", is_equal_to_sum_even(n) ? "True" : "False");
    return 0;
}
