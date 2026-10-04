#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

void encrypt(const char *s, char *result) {
    for (int i = 0; s[i]; i++) {
        if (islower(s[i])) {
            result[i] = ((s[i] - 'a' + 4) % 26) + 'a';
        } else {
            result[i] = s[i];
        }
    }
    result[strlen(s)] = 0;
}

int main() {
    char s[1000], result[1000];
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;
    encrypt(s, result);
    printf("%s\n", result);
    return 0;
}

