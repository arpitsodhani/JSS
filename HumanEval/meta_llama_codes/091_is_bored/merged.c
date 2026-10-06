#include <stdio.h>

int count_boredoms(char* s) {
    int count = 0;
    int i = 0;
    
    while (s[i] != '\0' && s[i] != '\n') {
        
        while (s[i] == ' ') i++;
        
        
        if (s[i] == 'I' && (s[i+1] == ' ' || s[i+1] == '.' || s[i+1] == '?' || s[i+1] == '!' || s[i+1] == '\0')) {
            count++;
        }
        
        
        while (s[i] != '\0' && s[i] != '.' && s[i] != '?' && s[i] != '!' && s[i] != '\n') {
            i++;
        }
        
        if (s[i] == '.' || s[i] == '?' || s[i] == '!') i++;
    }
    
    return count;
}

int main() {
    char s[10000];
    fgets(s, 10000, stdin);
    int length = 0;
    while (s[length] != '\0' && s[length] != '\n') ++length;
    s[length] = '\0';
    if (length >= 2 && s[0] == '"' && s[length - 1] == '"') {
        for (int i = 0; i < length - 1; ++i) s[i] = s[i + 1];
        s[length - 2] = '\0';
    }
    printf("%d\n", count_boredoms(s));
    return 0;
}
