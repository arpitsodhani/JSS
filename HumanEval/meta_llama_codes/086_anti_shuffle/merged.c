#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void anti_shuffle_word(char *word, char *result) {
    int len = strlen(word);
    char temp[100];
    strcpy(temp, word);
    for (int i = 0; i < len - 1; i++) {
        for (int j = 0; j < len - i - 1; j++) {
            if (temp[j] > temp[j + 1]) {
                char t = temp[j];
                temp[j] = temp[j + 1];
                temp[j + 1] = t;
            }
        }
    }
    strcpy(result, temp);
}

int main(void) {
    char s[1000];
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;
    char result[1000] = "";
    char word[100];
    int word_idx = 0;
    for (int i = 0; i <= strlen(s); i++) {
        if (s[i] == ' ' || s[i] == '\0') {
            word[word_idx] = '\0';
            char sorted_word[100];
            anti_shuffle_word(word, sorted_word);
            strcat(result, sorted_word);
            if (s[i] == ' ') strcat(result, " ");
            word_idx = 0;
        } else {
            word[word_idx++] = s[i];
        }
    }
    printf("%s\n", result);
    return 0;
}
