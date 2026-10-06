#include <ctype.h>
#include <stdio.h>
#include <string.h>

int check_case_consistency(char keys[][100], int n) {
    if (n == 0) return 0;
    
    int has_lower = 0, has_upper = 0;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; keys[i][j] != '\0'; j++) {
            if (keys[i][j] >= 'a' && keys[i][j] <= 'z') {
                has_lower = 1;
            } else if (keys[i][j] >= 'A' && keys[i][j] <= 'Z') {
                has_upper = 1;
            }
        }
    }
    
    return (has_lower && !has_upper) || (!has_lower && has_upper);
}

int main() {
    char input[10000];
    size_t used = fread(input, 1, sizeof(input) - 1, stdin);
    input[used] = '\0';
    char keys[100][100];
    int n = 0, invalid = 0;
    for (size_t i = 0; i < used;) {
        if (input[i] != '"') { ++i; continue; }
        size_t start = ++i, end = start;
        while (end < used && input[end] != '"') ++end;
        if (end == used) { invalid = 1; break; }
        size_t next = end + 1;
        while (next < used && isspace((unsigned char)input[next])) ++next;
        if (next >= used || input[next] != ':') { i = end + 1; continue; }
        size_t length = end - start;
        if (length == 0 || length >= sizeof(keys[0])) { invalid = 1; break; }
        int digits_only = 1;
        for (size_t j = 0; j < length; ++j) {
            keys[n][j] = input[start + j];
            if (!isdigit((unsigned char)keys[n][j])) digits_only = 0;
        }
        keys[n++][length] = '\0';
        if (digits_only) invalid = 1;
        i = end + 1;
    }
    if (!invalid && check_case_consistency(keys, n)) {
        printf("True\n");
    } else {
        printf("False\n");
    }
    
    return 0;
}
