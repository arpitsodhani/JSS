#include <stdio.h>

double square_root(double value) {
    if (value <= 0) return 0;
    double estimate = value >= 1 ? value : 1;
    for (int i = 0; i < 40; ++i) estimate = (estimate + value / estimate) / 2.0;
    return estimate;
}

double triangle_area(double a, double b, double c) {
    if (a <= 0 || b <= 0 || c <= 0 || a + b <= c || a + c <= b || b + c <= a) return -1;
    double s = (a + b + c) / 2.0;
    return square_root(s * (s - a) * (s - b) * (s - c));
}

int main(void) {
    double a, b, c;
    if (scanf("%lf %lf %lf", &a, &b, &c) != 3) return 1;
    double area = triangle_area(a, b, c);
    if (area < 0) printf("-1\n");
    else printf("%.2f\n", area);
    return 0;
}
