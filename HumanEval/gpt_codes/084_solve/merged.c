#include <stdio.h>

void solve_case_swap(char *s, char *result) {
    int has_alpha = 0;
    for (int i = 0; s[i]; i++) {
        if (isalpha(s[i])) {
            has_alpha = 1;
            break;
        }
    }
    if (!has_alpha) {
        for (int i = 0; s[i]; i++) {
            result[strlen(s) - 1 - i] = s[i];
        }
        result[strlen(s)] = '\0';
    } else {
        for (int i = 0; s[i]; i++) {
            if (islower(s[i])) {
                result[i] = toupper(s[i]);
            } else if (isupper(s[i])) {
                result[i] = tolower(s[i]);
            } else {
                result[i] = s[i];
            }
        }
        result[strlen(s)] = '\0';
    }
}

int main(void) {
    char s[1000];
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;
    char result[1000];
    solve_case_swap(s, result);
    printf("%s\n", result);
    return 0;
}
