#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, k, a[1000], s = 0;
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    for (int i = 0; i < k; i++) if (abs(a[i]) < 100) s += a[i];
    printf("%d\n", s);
    return 0;
}
