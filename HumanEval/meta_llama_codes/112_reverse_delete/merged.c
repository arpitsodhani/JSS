#include <stdio.h>
#include <string.h>

void process_reverse_delete(char *s, char *c, char *result, int *is_palindrome) {
    int j = 0;
    for (int i = 0; s[i]; i++) {
        int should_delete = 0;
        for (int k = 0; c[k]; k++) {
            if (s[i] == c[k]) {
                should_delete = 1;
                break;
            }
        }
        if (!should_delete) {
            result[j++] = s[i];
        }
    }
    result[j] = '\0';
    *is_palindrome = 1;
    for (int i = 0; i < j / 2; i++) {
        if (result[i] != result[j - 1 - i]) {
            *is_palindrome = 0;
            break;
        }
    }
}

int main(void) {
    char s[1000], c[1000];
    scanf("%s %s", s, c);
    char result[1000];
    int is_palindrome;
    process_reverse_delete(s, c, result, &is_palindrome);
    printf("(%s %s)\n", result, is_palindrome ? "True" : "False");
    return 0;
}
