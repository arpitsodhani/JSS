#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    printf("%s\n", (n >= 8 && !(n & 1)) ? "True" : "False");
    return 0;
}
