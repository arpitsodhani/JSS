#include <stdio.h>
#include <string.h>

int palindrome_suffix_start(const char *s, int len) {
    for (int start = 0; start < len; ++start) {
        int left = start, right = len - 1;
        while (left < right && s[left] == s[right]) {
            ++left;
            --right;
        }
        if (left >= right) return start;
    }
    return len;
}

int main(void) {
    char s[1000];
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;
    int len = strlen(s);
    int suffix_start = palindrome_suffix_start(s, len);
    printf("%s", s);
    for (int i = suffix_start - 1; i >= 0; --i) {
        printf("%c", s[i]);
    }
    printf("\n");
    return 0;
}
