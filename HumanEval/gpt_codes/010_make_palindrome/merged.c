#include <stdio.h>
#include <string.h>

int find_palindrome_suffix_len(char *s, int len) {
    for (int i = 0; i < len; i++) {
        int l = i, r = len - 1;
        int is_palindrome = 1;
        while (l < r) {
            if (s[l] != s[len - 1 - (r - l)]) {
                is_palindrome = 0;
                break;
            }
            l++;
        }
        if (is_palindrome || l >= r) {
            return len - i;
        }
    }
    return 0;
}

int main(void) {
    char s[1000];
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;
    int len = strlen(s);
    int suffix_len = find_palindrome_suffix_len(s, len);
    printf("%s", s);
    for (int i = suffix_len; i < len; i++) {
        printf("%c", s[len - 1 - i]);
    }
    printf("\n");
    return 0;
}
