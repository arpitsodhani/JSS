#include <stdio.h>

int main(void) {
    int num;
    scanf("%d", &num);
    for (int i = 0; i < num; i++) {
        printf("%d", num + 2 * i);
    }
    printf("\n");
    return 0;
}
