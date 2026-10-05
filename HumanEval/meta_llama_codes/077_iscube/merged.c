#include <math.h>
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int abs_n = (n < 0) ? -n : n;
    int rt = (int)round(cbrt(abs_n));
    printf("%s\n", (rt * rt * rt == abs_n) ? "True" : "False");
    return 0;
}
