#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <math.h>

long long compute_cross_product_term(long long x1, long long y1, long long x2, long long y2) {
    return x1 * y2 - x2 * y1;
}

long long accumulate_polygon_area_terms(int n, long long *x, long long *y) {
    long long area_sum = 0;
    for (int i = 0; i < n; i++) {
        int next = (i + 1) % n;
        area_sum += compute_cross_product_term(x[i], y[i], x[next], y[next]);
    }
    return area_sum;
}

double compute_polygon_area(int n, long long *x, long long *y) {
    long long area_sum = accumulate_polygon_area_terms(n, x, y);
    return fabs(area_sum) / 2.0;
}

int main() {
    int n;
    long long x[10005], y[10005];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld", &x[i], &y[i]);
    }
    printf("%.1f\n", compute_polygon_area(n, x, y));
    return 0;
}