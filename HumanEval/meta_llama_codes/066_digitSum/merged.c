#include <ctype.h>
#include <stdio.h>
#include <string.h>

int compute_digit_sum(char *s) {
    int sum = 0;
    for (int i = 0; s[i]; i++) {
        if (isupper(s[i])) {
            sum += s[i];
        }
    }
    return sum;
}

int main(void) {
    char s[1000];
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;
    int result = compute_digit_sum(s);
    printf("%d\n", result);
    return 0;
}
