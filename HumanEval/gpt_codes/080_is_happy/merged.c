#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int check_length(const char *s) {
    int len = strlen(s);
    return len >= 3;
}

int check_consecutive(const char *s) {
    int len = strlen(s);
    for (int i = 0; i < len - 2; i++) {
        if (s[i] == s[i+1] || s[i] == s[i+2] || s[i+1] == s[i+2]) {
            return 0;
        }
    }
    return 1;
}

int is_happy(const char *s) {
    if (!check_length(s)) return 0;
    return check_consecutive(s);
}

int main() {
    char s[1000];
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;
    printf("%s\n", is_happy(s) ? "True" : "False");
    return 0;
}

