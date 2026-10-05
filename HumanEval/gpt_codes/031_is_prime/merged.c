#include <stdio.h>

int main(void) {
    int value;
    scanf("%d", &value);
    if (value < 2) {
        printf("False\n");
        return 0;
    }
    for (int div = 2; div * div <= value; div++) {
        if (value % div == 0) {
            printf("False\n");
            return 0;
        }
    }
    printf("True\n");
    return 0;
}
