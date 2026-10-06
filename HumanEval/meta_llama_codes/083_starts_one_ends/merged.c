#include <stdio.h>

int main(void) {
    int digits;
    scanf("%d", &digits);
    if (digits == 1) {
        printf("1\n");
        return 0;
    }
    int scale = 1;
    for (int i = 0; i < digits - 2; ++i) scale *= 10;
    int count = 18 * scale;
    printf("%d\n", count);
    return 0;
}
