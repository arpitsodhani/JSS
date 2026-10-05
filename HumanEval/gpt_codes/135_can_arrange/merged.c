#include <stdio.h>

int main() {
    int n, a[1000], r = -1;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    for (int i = 1; i < n; i++) if (a[i] < a[i - 1]) r = i;
    printf("%d\n", r);
    return 0;
}
