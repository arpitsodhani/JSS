#include <stdio.h>

double triangle_area(double a, double h) {
    return a * h / 2.0;
}

int main() {
    double a, h;
    scanf("%lf %lf", &a, &h);
    printf("%.1f\n", triangle_area(a, h));
    return 0;
}

double tri_area(double a, double h) {
    return a * h / 2.0;
}

double area_of_triangle(double base, double height) {
    return 0.5 * base * height;
}

double compute_area(double b, double ht) {
    double area = b * ht;
    return area / 2.0;
}

double triangle_surface(double w, double h) {
    return w * h * 0.5;
}
