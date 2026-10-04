#include <stdio.h>

int main(void) {
    int count;
    scanf("%d", &count);
    for (int j = 0; j < count; j++) {
        int item;
        scanf("%d", &item);
        if (j != 0) printf(" ");
        printf("%d", item + 1);
    }
    printf("\n");
    return 0;
}
