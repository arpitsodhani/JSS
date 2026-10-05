#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    if (n == 0) {
        printf("0\n");
        return 0;
    }
    if (n == 1 || n == 2) {
        printf("%d\n", n == 1 ? 0 : 1);
        return 0;
    }
    int a = 0, b = 0, c = 1;
    for (int i = 3; i <= n; i++) {
        int next = a + b + c;
        a = b;
        b = c;
        c = next;
    }
    printf("%d\n", c);
    return 0;
}
