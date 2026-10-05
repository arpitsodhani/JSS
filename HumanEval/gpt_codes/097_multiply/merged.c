#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int num1, num2;
    scanf("%d %d", &num1, &num2);
    printf("%d\n", abs(num1 % 10) * abs(num2 % 10));
    return 0;
}
