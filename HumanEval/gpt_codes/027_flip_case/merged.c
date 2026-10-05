#include <stdio.h>
#include <string.h>

char flip_char(char c) {
    if (c >= 'a' && c <= 'z') {
        return c - 32;
    } else if (c >= 'A' && c <= 'Z') {
        return c + 32;
    }
    return c;
}

int main() {
    char str[1000];
    fgets(str, 1000, stdin);
    
    for (int i = 0; str[i] != '\0' && str[i] != '\n'; i++) {
        str[i] = flip_char(str[i]);
    }
    
    printf("%s", str);
    if (str[strlen(str)-1] != '\n') printf("\n");
    return 0;
}
