#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    for (int i = 0; i <= n; i++) {
        if (i > 0) printf(" ");
        printf("%d", i);
    }
    printf("\n");
    return 0;
}
