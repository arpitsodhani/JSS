#include <stdio.h>
#include <string.h>

int main(void) {
    char sa[64], sb[64], sc[64];
    if (scanf("%63s %63s %63s", sa, sb, sc) != 3) return 1;
    if (strchr(sa, '.') || strchr(sb, '.') || strchr(sc, '.')) {
        printf("False\n");
        return 0;
    }
    long long ai, bi, ci;
    if (sscanf(sa, "%lld", &ai) != 1 || sscanf(sb, "%lld", &bi) != 1 || sscanf(sc, "%lld", &ci) != 1) return 1;
    if (ai + bi == ci || ai + ci == bi || bi + ci == ai) {
        printf("True\n");
    } else {
        printf("False\n");
    }
    return 0;
}
