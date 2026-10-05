#include <stdio.h>
#include <string.h>

void reverse_and_swap_case(char* s, char* result) {
    int len = strlen(s);
    int has_letter = 0;
    
    for (int i = 0; i < len; i++) {
        if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z')) {
            has_letter = 1;
            break;
        }
    }
    
    for (int i = 0; i < len; i++) {
        char c = s[len - 1 - i];
        if (has_letter) {
            if (c >= 'a' && c <= 'z') {
                result[i] = c - 32;
            } else if (c >= 'A' && c <= 'Z') {
                result[i] = c + 32;
            } else {
                result[i] = c;
            }
        } else {
            result[i] = c;
        }
    }
    result[len] = '\0';
}

int main() {
    char s[1000];
    fgets(s, 1000, stdin);
    
    
    int len = strlen(s);
    if (s[len - 1] == '\n') s[len - 1] = '\0';
    
    char result[1000];
    reverse_and_swap_case(s, result);
    
    printf("%s\n", result);
    return 0;
}
