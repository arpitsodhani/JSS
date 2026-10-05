#include <stdio.h>

int is_vowel(char c) {
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
}

int main() {
    char str[1000];
    fgets(str, 1000, stdin);
    
    for (int i = 0; str[i] != '\0'; i++) {
        if (!is_vowel(str[i])) {
            printf("%c", str[i]);
        }
    }
    
    return 0;
}
