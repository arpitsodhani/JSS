#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int abs_n = (n < 0) ? -n : n;
    int rt = 0;
    while ((rt + 1) <= 1290 && (rt + 1) * (rt + 1) * (rt + 1) <= abs_n) ++rt;
    printf("%s\n", (rt * rt * rt == abs_n) ? "True" : "False");
    return 0;
}
