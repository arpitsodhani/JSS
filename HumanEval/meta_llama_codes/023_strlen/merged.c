#include <stdio.h>

int main(void) {
    char buffer[10001];
    if (scanf("%10000[^\n]", buffer) != 1) {
        printf("0\n");
    } else {
        int n = 0;
        while (buffer[n] != '\0') n++;
        printf("%d\n", n);
    }
    return 0;
}
