#include <stdio.h>

int is_integer(const char *text) {
    if (text[0] == '\0') return 0;
    for (int i = 0; text[i]; ++i) {
        if (text[i] < '0' || text[i] > '9') return 0;
    }
    return 1;
}

void print_integers(char strs[][100], int n) {
    int first = 1;
    for (int i = 0; i < n; i++) {
        if (!is_integer(strs[i])) continue;
        if (!first) printf(" ");
        printf("%s", strs[i]);
        first = 0;
    }
    printf("\n");
}

int main(void) {
    int n;
    scanf("%d", &n);
    getchar();
    char strs[n][100];
    for (int i = 0; i < n; i++) {
        fgets(strs[i], sizeof(strs[i]), stdin);
        strs[i][strcspn(strs[i], "\n")] = 0;
    }
    print_integers(strs, n);
    return 0;
}
