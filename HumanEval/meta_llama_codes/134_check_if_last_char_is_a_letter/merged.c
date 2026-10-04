#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char s[1000];
    fgets(s, 1000, stdin);
    int len = strlen(s);
    if (s[len - 1] == '\n') s[--len] = 0;
    printf("%s\n", (len > 0 && isalpha(s[len - 1]) && (len == 1 || s[len - 2] == ' ')) ? "True" : "False");
    return 0;
}
