#include <stdio.h>

int main() {
    int n, a[1000], s = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    for (int i = 0; i < n; i += 2) if (a[i] & 1) s += a[i];
    printf("%d\n", s);
    return 0;
}
