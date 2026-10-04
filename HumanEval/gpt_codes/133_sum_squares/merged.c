#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int sum_squares(int n, double lst[]) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        int val = (int)ceil(lst[i]);
        sum += val * val;
    }
    return sum;
}

int main() {
    int n;
    scanf("%d", &n);
    double lst[n];
    for (int i = 0; i < n; i++) {
        scanf("%lf", &lst[i]);
    }
    printf("%d\n", sum_squares(n, lst));
    return 0;
}
