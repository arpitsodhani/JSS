#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int is_valid(const char *s) {
    int count = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] == '(') count++;
        else if (s[i] == ')') count--;
        if (count < 0) return 0;
    }
    return count == 0;
}

const char* match_parens(const char *s1, const char *s2) {
    char combined1[20000], combined2[20000];
    strcpy(combined1, s1);
    strcat(combined1, s2);
    strcpy(combined2, s2);
    strcat(combined2, s1);
    
    if (is_valid(combined1) || is_valid(combined2)) {
        return "Yes";
    }
    return "No";
}

int main() {
    char s1[10000], s2[10000];
    fgets(s1, sizeof(s1), stdin);
    s1[strcspn(s1, "\n")] = 0;
    fgets(s2, sizeof(s2), stdin);
    s2[strcspn(s2, "\n")] = 0;
    
    printf("%s\n", match_parens(s1, s2));
    return 0;
}

