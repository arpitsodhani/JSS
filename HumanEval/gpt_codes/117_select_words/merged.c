#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int count_consonants(const char *word) {
    int count = 0;
    for (int i = 0; word[i]; i++) {
        char c = tolower(word[i]);
        if (isalpha(c) && c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
            count++;
        }
    }
    return count;
}

void select_words(const char *s, int n, char result[][100], int *result_size) {
    *result_size = 0;
    char temp[10000];
    strcpy(temp, s);
    
    char *token = strtok(temp, " ");
    while (token != NULL) {
        if (count_consonants(token) == n) {
            strcpy(result[(*result_size)++], token);
        }
        token = strtok(NULL, " ");
    }
}

int main() {
    char s[10000];
    int n;
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;
    scanf("%d", &n);
    
    char result[1000][100];
    int result_size;
    select_words(s, n, result, &result_size);
    
    for (int i = 0; i < result_size; i++) {
        printf("%s", result[i]);
        if (i < result_size - 1) printf(" ");
    }
    printf("\n");
    return 0;
}

