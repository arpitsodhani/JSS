#include <stdio.h>
#include <string.h>

int main(void) {
    char input[1000];
    fgets(input, sizeof(input), stdin);
    
    int depth = 0;
    char group[1000];
    int pos = 0;
    
    for (int i = 0; input[i] != '\0' && input[i] != '\n'; i++) {
        if (input[i] == '(') {
            group[pos++] = '(';
            depth++;
        } else if (input[i] == ')') {
            group[pos++] = ')';
            depth--;
            if (depth == 0) {
                group[pos] = '\0';
                printf("%s\n", group);
                pos = 0;
            }
        }
    }
    return 0;
}

void print_group(char *s, int len) {
    for (int i = 0; i < len; i++) {
        printf("%c", s[i]);
    }
    printf("\n");
}
