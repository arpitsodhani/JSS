#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void words_string(const char *s, char words[][100], int *count) {
    *count = 0;
    char temp[1000];
    strcpy(temp, s);
    
    int word_start = 0;
    int word_len = 0;
    
    for (int i = 0; temp[i]; i++) {
        if (temp[i] == ',') {
            temp[i] = ' ';
        }
    }
    
    char *token = strtok(temp, " ");
    while (token != NULL) {
        strcpy(words[*count], token);
        (*count)++;
        token = strtok(NULL, " ");
    }
}

void run(void) {

    char s[10000];
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;
    
    char words[1000][100];
    int count;
    words_string(s, words, &count);
    
    for (int i = 0; i < count; i++) {
        printf("%s", words[i]);
        if (i < count - 1) printf(" ");
    }
    printf("\n");
}

int main() {
    run();
    return 0;
}
