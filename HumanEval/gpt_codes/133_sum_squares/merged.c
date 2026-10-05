#include <stdio.h>
#include <math.h>

int main() {
    int n, s = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        double x;
        scanf("%lf", &x);
        int c = (int)ceil(x);
        s += c * c;
    }
    printf("%d\n", s);
    return 0;
}
