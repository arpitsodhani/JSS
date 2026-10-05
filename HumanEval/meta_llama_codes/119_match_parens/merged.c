#include <stdio.h>
#include <string.h>

int can_match_parens(char *s1, char *s2) {
    char combined[2000];
    strcpy(combined, s1);
    strcat(combined, s2);
    int balance = 0;
    for (int i = 0; combined[i]; i++) {
        if (combined[i] == '(') balance++;
        else if (combined[i] == ')') balance--;
        if (balance < 0) return 0;
    }
    if (balance != 0) return 0;
    strcpy(combined, s2);
    strcat(combined, s1);
    balance = 0;
    for (int i = 0; combined[i]; i++) {
        if (combined[i] == '(') balance++;
        else if (combined[i] == ')') balance--;
        if (balance < 0) return 0;
    }
    return balance == 0;
}

int main(void) {
    char s1[1000], s2[1000];
    scanf("%s %s", s1, s2);
    if (can_match_parens(s1, s2)) {
        printf("Yes\n");
    } else {
        printf("No\n");
    }
    return 0;
}
