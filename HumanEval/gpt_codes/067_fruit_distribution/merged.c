#include <stdio.h>

int main(void) {
    int first, second, all;
    scanf("%d %d %d", &first, &second, &all);
    printf("%d\n", all - first - second);
    return 0;
}
