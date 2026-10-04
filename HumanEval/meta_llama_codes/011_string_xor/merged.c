#include <stdio.h>
#include <string.h>

int main(void) {
    char a[1001], b[1001], result[1001];
    scanf("%s %s", a, b);
    int len = strlen(a);
    for (int i = 0; i < len; i++) {
        result[i] = (a[i] == b[i]) ? '0' : '1';
    }
    result[len] = '\0';
    printf("%s\n", result);
    return 0;
}
