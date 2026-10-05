#include <math.h>
#include <stdio.h>

int main(void) {
    double a, b, c;
    scanf("%lf %lf %lf", &a, &b, &c);
    int ai = (int)a, bi = (int)b, ci = (int)c;
    if (a != ai || b != bi || c != ci) {
        printf("False\n");
        return 0;
    }
    if (ai + bi == ci || ai + ci == bi || bi + ci == ai) {
        printf("True\n");
    } else {
        printf("False\n");
    }
    return 0;
}
