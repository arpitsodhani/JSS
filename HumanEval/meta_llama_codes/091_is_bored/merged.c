#include <stdio.h>

int count_boredoms(char* s) {
    int count = 0;
    int i = 0;
    
    while (s[i] != '\0' && s[i] != '\n') {
        
        while (s[i] == ' ') i++;
        
        
        if (s[i] == 'I' && (s[i+1] == ' ' || s[i+1] == '.' || s[i+1] == '?' || s[i+1] == '!')) {
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
    
    printf("%d\n", count_boredoms(s));
    return 0;
}
