#include <stdio.h>

int main() {
    int n, a[1000];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    for (int i = 0; i < n - 1; i++) if (a[i] >= a[i + 1]) { printf("False\n"); return 0; }
    printf("True\n");
    return 0;
}
