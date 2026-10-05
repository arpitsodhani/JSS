#include <stdio.h>

int is_upper_vowel(char c) {
    return (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
}

int main() {
    char s[1000];
    fgets(s, 1000, stdin);
    
    int count = 0;
    for (int i = 0; s[i] != '\0' && s[i] != '\n'; i++) {
        if (i % 2 == 0 && is_upper_vowel(s[i])) {
            count++;
        }
    }
    
    printf("%d\n", count);
    return 0;
}
