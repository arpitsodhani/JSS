#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int cmp(const void *a, const void *b) {
    return *(char*)a - *(char*)b;
}

void sort_string(char *s) {
    qsort(s, strlen(s), 1, cmp);
}

void anti_shuffle(const char *s, char *result) {
    char word[1000];
    int word_idx = 0, res_idx = 0;
    
    for (int i = 0; s[i]; i++) {
        if (s[i] == ' ') {
            word[word_idx] = 0;
            sort_string(word);
            strcpy(result + res_idx, word);
            res_idx += word_idx;
            result[res_idx++] = ' ';
            word_idx = 0;
        } else {
            word[word_idx++] = s[i];
        }
    }
    word[word_idx] = 0;
    sort_string(word);
    strcpy(result + res_idx, word);
    res_idx += word_idx;
    result[res_idx] = 0;
}

int main() {
    char s[10000], result[10000];
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;
    anti_shuffle(s, result);
    printf("%s\n", result);
    return 0;
}

