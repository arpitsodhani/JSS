#include <stdio.h>

int count_distinct_chars(char *s) {
    int seen[256] = {0};
    int count = 0;
    for (int i = 0; s[i]; i++) {
        char c = tolower(s[i]);
        if (!seen[(unsigned char)c]) {
            seen[(unsigned char)c] = 1;
            count++;
        }
    }
    return count;
}

int main(void) {
    char s[1000];
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;
    int result = count_distinct_chars(s);
    printf("%d\n", result);
    return 0;
}
