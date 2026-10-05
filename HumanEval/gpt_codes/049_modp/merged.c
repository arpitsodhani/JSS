#include <stdio.h>

int main(void) {
    int n, p;
    scanf("%d %d", &n, &p);
    int pow2 = 1;
    for (int j = 0; j < n; j++) {
        pow2 = (pow2 * 2) % p;
    }
    printf("%d\n", pow2);
    return 0;
}
