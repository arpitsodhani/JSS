#include <stdio.h>

int main(void) {
    int low, high;
    scanf("%d %d", &low, &high);
    if (high < low) {
        printf("-1\n");
    } else if (high % 2 == 0) {
        printf("%d\n", high);
    } else if (high - 1 >= low) {
        printf("%d\n", high - 1);
    } else {
        printf("-1\n");
    }
    return 0;
}
