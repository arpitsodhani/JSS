#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int is_vowel(char c) {
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int is_consonant(char c) {
    return isalpha(c) && !is_vowel(c);
}

char get_closest_vowel(const char *word) {
    int len = strlen(word);
    if (len < 3) return '\0';
    
    for (int i = len - 2; i >= 1; i--) {
        if (is_vowel(word[i]) && is_consonant(word[i-1]) && is_consonant(word[i+1])) {
            return word[i];
        }
    }
    return '\0';
}

int main() {
    char word[10000];
    fgets(word, sizeof(word), stdin);
    word[strcspn(word, "\n")] = 0;
    
    char result = get_closest_vowel(word);
    if (result == '\0') {
        printf("\n");
    } else {
        printf("%c\n", result);
    }
    return 0;
}

