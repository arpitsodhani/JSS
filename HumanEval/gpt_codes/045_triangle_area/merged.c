#include <stdio.h>

int main(void) {
    double b, h;
    scanf("%lf %lf", &b, &h);
    double area = b * h * 0.5;
    if (area == (int)area) {
        printf("%.1f\n", area);
    } else {
        printf("%g\n", area);
    }
    return 0;
}
