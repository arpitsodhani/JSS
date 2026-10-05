#include <stdio.h>
#include <string.h>

void extract_words(char *s, char words[][100], int *count) {
    *count = 0;
    int in_word = 0;
    int word_idx = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] == ' ' || s[i] == ',') {
            if (in_word) {
                words[*count][word_idx] = '\0';
                (*count)++;
                in_word = 0;
                word_idx = 0;
            }
        } else {
            if (!in_word) {
                in_word = 1;
            }
            words[*count][word_idx++] = s[i];
        }
    }
    if (in_word) {
        words[*count][word_idx] = '\0';
        (*count)++;
    }
}

int main(void) {
    char s[1000];
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;
    char words[100][100];
    int count;
    extract_words(s, words, &count);
    for (int i = 0; i < count; i++) {
        printf("%s", words[i]);
        if (i < count - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
