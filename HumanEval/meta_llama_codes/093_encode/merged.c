#include <stdio.h>

char encode_char(char c) {
    if (c >= 'a' && c <= 'z') {
        switch(c) {
            case 'a': return 'C';
            case 'e': return 'G';
            case 'i': return 'K';
            case 'o': return 'Q';
            case 'u': return 'W';
            default:
                if (c >= 'a' && c <= 'z') {
                    return c - 32;  
                }
                return c;
        }
    } else if (c >= 'A' && c <= 'Z') {
        switch(c) {
            case 'A': return 'c';
            case 'E': return 'g';
            case 'I': return 'k';
            case 'O': return 'q';
            case 'U': return 'w';
            default:
                return c + 32;  
        }
    }
    return c;
}

int main() {
    char str[1000];
    fgets(str, 1000, stdin);
    
    for (int i = 0; str[i] != '\0' && str[i] != '\n'; i++) {
        str[i] = encode_char(str[i]);
    }
    
    printf("%s", str);
    return 0;
}
