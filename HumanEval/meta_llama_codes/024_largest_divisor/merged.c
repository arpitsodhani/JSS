#include <stdio.h>

int main(void) {
    int number;
    scanf("%d", &number);
    for (int i = number / 2; i > 0; i--) {
        if (number % i == 0) {
            printf("%d\n", i);
            return 0;
        }
    }
    printf("1\n");
    return 0;
}
