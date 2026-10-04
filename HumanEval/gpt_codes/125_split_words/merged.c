#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

void split_words(const char *txt, char result[][100], int *count) {
    *count = 0;
    
    int has_space = 0;
    for (int i = 0; txt[i]; i++) {
        if (txt[i] == ' ') {
            has_space = 1;
            break;
        }
    }
    
    if (has_space) {
        char temp[1000];
        strcpy(temp, txt);
        char *token = strtok(temp, " ");
        while (token != NULL) {
            strcpy(result[*count], token);
            (*count)++;
            token = strtok(NULL, " ");
        }
        return;
    }
    
    int has_comma = 0;
    for (int i = 0; txt[i]; i++) {
        if (txt[i] == ',') {
            has_comma = 1;
            break;
        }
    }
    
    if (has_comma) {
        char temp[1000];
        strcpy(temp, txt);
        char *token = strtok(temp, ",");
        while (token != NULL) {
            strcpy(result[*count], token);
            (*count)++;
            token = strtok(NULL, ",");
        }
        return;
    }
    
    int lowercase_count = 0;
    for (int i = 0; txt[i]; i++) {
        if (islower(txt[i]) && (txt[i] - 'a') % 2 == 1) {
            lowercase_count++;
        }
    }
    
    sprintf(result[0], "%d", lowercase_count);
    *count = 1;
}

int main() {
    char txt[1000];
    fgets(txt, sizeof(txt), stdin);
    txt[strcspn(txt, "\n")] = 0;
    
    char result[100][100];
    int count;
    split_words(txt, result, &count);
    
    for (int i = 0; i < count; i++) {
        printf("%s", result[i]);
        if (i < count - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
