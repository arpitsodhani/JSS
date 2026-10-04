#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_target(long long *n) {
    scanf("%lld", n);
}

int construct_palindrome_formula(long long n, char *result) {
    if (n == 0) {
        strcpy(result, "0+0");
        return 1;
    }
    char formula[205] = "";
    while (n > 0) {
        if (n >= 9) {
            if (strlen(formula) > 0) strcat(formula, "+");
            strcat(formula, "9");
            n -= 9;
        } else {
            if (strlen(formula) > 0) strcat(formula, "+");
            char digit[2] = {(char)('0' + n), '\0'};
            strcat(formula, digit);
            n = 0;
        }
    }
    int len = strlen(formula);
    strcpy(result, formula);
    result[len] = '+';
    for (int i = len - 1; i >= 0; i--) result[len + (len - i)] = formula[i];
    result[2 * len + 1] = '\0';
    int is_pal = 1;
    int total_len = strlen(result);
    for (int i = 0; i < total_len / 2; i++) {
        if (result[i] != result[total_len - 1 - i]) {
            is_pal = 0;
            break;
        }
    }
    return is_pal;
}

int main() {
    long long n;
    char result[405];
    read_target(&n);
    if (construct_palindrome_formula(n, result)) {
        printf("%s\n", result);
    } else {
        printf("-1\n");
    }
    return 0;
}
