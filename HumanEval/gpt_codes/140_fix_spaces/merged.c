#include <stdio.h>

void fix_spaces(char* text, char* result) {
    int i = 0, j = 0;
    int space_count = 0;
    
    while (text[i] != '\0' && text[i] != '\n') {
        if (text[i] == ' ') {
            space_count++;
        } else {
            if (space_count > 0) {
                if (space_count == 1) {
                    result[j++] = '_';
                } else if (space_count == 2) {
                    result[j++] = '_';
                    result[j++] = '_';
                } else {
                    result[j++] = '-';
                }
                space_count = 0;
            }
            result[j++] = text[i];
        }
        i++;
    }
    
    if (space_count > 0) {
        if (space_count == 1) {
            result[j++] = '_';
        } else if (space_count == 2) {
            result[j++] = '_';
            result[j++] = '_';
        } else {
            result[j++] = '-';
        }
    }
    
    result[j] = '\0';
}

int main() {
    char text[10000];
    fgets(text, 10000, stdin);
    
    char result[10000];
    fix_spaces(text, result);
    
    printf("%s\n", result);
    return 0;
}
