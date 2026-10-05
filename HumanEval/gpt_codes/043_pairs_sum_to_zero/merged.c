#include <stdio.h>

int main(void) {
    int len;
    scanf("%d", &len);
    int items[len];
    for (int p = 0; p < len; p++) scanf("%d", &items[p]);
    for (int i = 0; i < len - 1; i++) {
        for (int j = i + 1; j < len; j++) {
            if (items[i] + items[j] == 0) {
                printf("True\n");
                return 0;
            }
        }
    }
    printf("False\n");
    return 0;
}
