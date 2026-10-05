#include <ctype.h>
#include <stdio.h>
#include <string.h>

char get_closest_vowel_in_word(char *word) {
    char vowels[] = "aeiouAEIOU";
    int len = strlen(word);
    for (int i = len - 2; i >= 1; i--) {
        int is_vowel = 0;
        for (int j = 0; vowels[j]; j++) {
            if (word[i] == vowels[j]) {
                is_vowel = 1;
                break;
            }
        }
        if (is_vowel) {
            int left_consonant = 1, right_consonant = 1;
            for (int j = 0; vowels[j]; j++) {
                if (word[i-1] == vowels[j]) left_consonant = 0;
                if (word[i+1] == vowels[j]) right_consonant = 0;
            }
            if (left_consonant && right_consonant) {
                return word[i];
            }
        }
    }
    return '\0';
}

int main(void) {
    char word[1000];
    scanf("%s", word);
    char result = get_closest_vowel_in_word(word);
    if (result == '\0') {
        printf("\n");
    } else {
        printf("%c\n", result);
    }
    return 0;
}
