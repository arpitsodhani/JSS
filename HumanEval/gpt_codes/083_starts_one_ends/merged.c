#include <math.h>
#include <stdio.h>

int main(void) {
    int digits;
    scanf("%d", &digits);
    if (digits == 1) {
        printf("1\n");
        return 0;
    }
    int count = 18 * (int)pow(10, digits - 2);
    printf("%d\n", count);
    return 0;
}
