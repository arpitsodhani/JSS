#include <stdio.h>

int check_balanced(char* str) {
    int depth = 0;
    for (int i = 0; str[i] != '\0' && str[i] != '\n'; i++) {
        if (str[i] == '<') {
            depth++;
        } else if (str[i] == '>') {
            depth--;
            if (depth < 0) return 0;
        }
    }
    return depth == 0;
}

int main() {
    char str[1000];
    fgets(str, 1000, stdin);
    
    if (check_balanced(str)) {
        printf("True\n");
    } else {
        printf("False\n");
    }
    
    return 0;
}
