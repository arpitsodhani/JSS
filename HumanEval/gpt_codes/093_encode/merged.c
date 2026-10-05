#include <stdio.h>

char encode_char(char c) {
    if (c >= 'a' && c <= 'z') {
        switch(c) {
            case 'a': return 'C';
            case 'e': return 'G';
            case 'i': return 'M';
            case 'o': return 'S';
            case 'u': return 'Y';
            default:
                if (c >= 'a' && c <= 'z') {
                    return c - 32;  // uppercase
                }
                return c;
        }
    } else if (c >= 'A' && c <= 'Z') {
        switch(c) {
            case 'A': return 'c';
            case 'E': return 'g';
            case 'I': return 'm';
            case 'O': return 's';
            case 'U': return 'y';
            default:
                return c + 32;  // lowercase
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
    
    printf("%s\n", str);
    return 0;
}
