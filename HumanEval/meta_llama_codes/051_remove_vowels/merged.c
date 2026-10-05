#include <stdio.h>

int is_vowel(char c) {
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
}

int main(void) {
    int ch;
    while ((ch = getchar()) != EOF) {
        if (!is_vowel((char)ch)) putchar(ch);
    }
    return 0;
}
