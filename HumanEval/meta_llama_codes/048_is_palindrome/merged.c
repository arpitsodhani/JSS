#include <stdio.h>
#include <string.h>

int check_palindrome(char* str) {
    int len = strlen(str);
    if (str[len-1] == '\n') len--;
    
    for (int i = 0; i < len / 2; i++) {
        if (str[i] != str[len - 1 - i]) {
            return 0;
        }
    }
    return 1;
}

int main() {
    char str[1000];
    fgets(str, 1000, stdin);
    
    if (check_palindrome(str)) {
        printf("True\n");
    } else {
        printf("False\n");
    }
    
    return 0;
}
