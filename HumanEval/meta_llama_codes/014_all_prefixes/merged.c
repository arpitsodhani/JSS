#include <stdio.h>
#include <string.h>

void print_all_prefixes(char *s, int len) {
    for (int i = 1; i <= len; i++) {
        for (int j = 0; j < i; j++) {
            printf("%c", s[j]);
        }
        printf("\n");
    }
    if (len == 0) printf("\n");
}

int main(void) {
    char s[1000];
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;
    int len = strlen(s);
    print_all_prefixes(s, len);
    return 0;
}
