#include <stdio.h>

double calculate_area(double a, double h) {
    if (a <= 0 || h <= 0) {
        return -1;
    }
    return (a * h) / 2.0;
}

int main() {
    double a, h;
    scanf("%lf %lf", &a, &h);
    
    double result = calculate_area(a, h);
    printf("%.2f\n", result);
    
    return 0;
}
