#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_dishes(int *n, char *s) {
    scanf("%d %s", n, s);
}

int check_consecutive_sweets(int n, char *s) {
    for (int i = 0; i < n - 1; i++) {
        if (s[i] == '1' && s[i + 1] == '1') return 0;
    }
    return 1;
}

int main() {
    int n;
    char s[105];
    read_dishes(&n, s);
    printf("%s\n", check_consecutive_sweets(n, s) ? "Yes" : "No");
    return 0;
}
