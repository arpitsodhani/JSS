#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void read_prices(int *r, int *g, int *b, char *c) {
    scanf("%d %d %d", r, g, b);
    scanf("%s", c);
}

int find_minimum_cost(int r, int g, int b, char *c) {
    int min = 1000;
    if (strcmp(c, "Red") != 0 && r < min) min = r;
    if (strcmp(c, "Green") != 0 && g < min) min = g;
    if (strcmp(c, "Blue") != 0 && b < min) min = b;
    return min;
}

int main() {
    int r, g, b;
    char c[10];
    read_prices(&r, &g, &b, c);
    printf("%d\n", find_minimum_cost(r, g, b, c));
    return 0;
}

