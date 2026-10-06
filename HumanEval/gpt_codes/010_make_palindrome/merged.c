#include <stdio.h>
#include <string.h>

int prefix_to_mirror(const char *s, int len) {
    for (int start = 0; start < len; ++start) {
        int palindrome = 1;
        for (int left = start, right = len - 1; left < right; ++left, --right) {
            if (s[left] != s[right]) { palindrome = 0; break; }
        }
        if (palindrome) return start;
    }
    return len;
}

int main(void) {
    char s[1000];
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;
    int len = strlen(s);
    int prefix_len = prefix_to_mirror(s, len);
    printf("%s", s);
    for (int i = prefix_len - 1; i >= 0; --i) {
        printf("%c", s[i]);
    }
    printf("\n");
    return 0;
}
