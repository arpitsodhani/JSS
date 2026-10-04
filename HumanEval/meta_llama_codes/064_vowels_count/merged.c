#include <ctype.h>
#include <stdio.h>
#include <string.h>

int count_vowels(char *s) {
    int count = 0;
    int len = strlen(s);
    for (int i = 0; i < len; i++) {
        char c = tolower(s[i]);
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            count++;
        }
    }
    if (len > 0 && tolower(s[len-1]) == 'y') {
        count++;
    }
    return count;
}

int main(void) {
    char s[1000];
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;
    int result = count_vowels(s);
    printf("%d\n", result);
    return 0;
}
