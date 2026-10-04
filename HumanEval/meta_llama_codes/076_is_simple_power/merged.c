#include <math.h>
#include <stdio.h>

int main(void) {
    int val, exp;
    scanf("%d %d", &val, &exp);
    if (exp == 1) {
        printf("%s\n", (val == 1) ? "True" : "False");
        return 0;
    }
    long long ans = 1;
    while (ans < val) ans *= exp;
    printf("%s\n", (ans == val) ? "True" : "False");
    return 0;
}
