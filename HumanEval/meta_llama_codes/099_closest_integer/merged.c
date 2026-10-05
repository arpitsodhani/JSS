#include <math.h>
#include <stdio.h>

int main(void) {
    double value;
    scanf("%lf", &value);
    double fractional = value - floor(value);
    if (fractional < 0.5) {
        printf("%d\n", (int)floor(value));
    } else if (fractional > 0.5) {
        printf("%d\n", (int)ceil(value));
    } else {
        printf("%d\n", (int)ceil(value));
    }
    return 0;
}
