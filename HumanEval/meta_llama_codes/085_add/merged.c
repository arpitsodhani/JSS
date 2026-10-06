#include <stdio.h>

int main(void) {
    int n, value, sum = 0;
    if (scanf("%d", &n) != 1) return 1;
    for (int i = 0; i < n; ++i) {
        if (scanf("%d", &value) != 1) return 1;
        if (i % 2 == 1 && value % 2 == 0) sum += value;
    }
    printf("%d\n", sum);
    return 0;
}
