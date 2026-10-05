#include <stdio.h>

int main(void) {
    int length;
    scanf("%d", &length);
    int largest;
    scanf("%d", &largest);
    for (int m = 1; m < length; m++) {
        int number;
        scanf("%d", &number);
        if (number > largest) largest = number;
    }
    printf("%d\n", largest);
    return 0;
}
