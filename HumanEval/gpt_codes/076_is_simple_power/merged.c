#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int is_simple_power(int x, int n) {
    if (x == 1) return 1;
    if (n <= 1) return 0;
    int power = n;
    while (power < x) power *= n;
    return power == x;
}

int main() {
    int x, n;
    scanf("%d %d", &x, &n);
    printf("%s\n", is_simple_power(x, n) ? "True" : "False");
    return 0;
}

