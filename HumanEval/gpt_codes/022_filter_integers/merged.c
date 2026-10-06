#include <ctype.h>
#include <stdio.h>
#include <string.h>

int is_integer(const char *text) {
    if (!text[0]) return 0;
    int start = (text[0] == '-' || text[0] == '+') ? 1 : 0;
    if (!text[start]) return 0;
    for (int i = start; text[i]; ++i) {
        if (!isdigit((unsigned char)text[i])) return 0;
    }
    return 1;
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
    int first = 1;
    for (int i = 0; i < n; ++i) {
        if (is_integer(strs[i])) {
            if (!first) printf(" ");
            printf("%s", strs[i]);
            first = 0;
        }
    }
    printf("\n");
    return 0;
}
