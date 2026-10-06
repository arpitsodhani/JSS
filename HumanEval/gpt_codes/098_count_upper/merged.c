#include <stdio.h>

int is_upper_vowel(char c) {
    return (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
}

int main() {
    char s[1000];
    fgets(s, 1000, stdin);
    int start = 0;
    int end = strcspn(s, "\n");
    if (end >= 2 && s[0] == '\'' && s[end - 1] == '\'') {
        start = 1;
        --end;
    }
    
    int count = 0;
    for (int i = start; i < end; i++) {
        if ((i - start) % 2 == 0 && is_upper_vowel(s[i])) {
            count++;
        }
    }
    
    printf("%d\n", count);
    return 0;
}
