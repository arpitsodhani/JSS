#include <stdio.h>

int main() {
    int n, p = 1, f = 0;
    scanf("%d", &n);
    for (; n; n /= 10) {
        int d = n % 10;
        if (d & 1) { p *= d; f = 1; }
    }
    printf("%d\n", f ? p : 0);
    return 0;
}
