#include <stdio.h>

int main(void) {
    double x;
    scanf("%lf", &x);
    double result = x - (int)x;
    printf("%g\n", result);
    return 0;
}

double get_fraction(double x) {
    return x - (int)x;
}
