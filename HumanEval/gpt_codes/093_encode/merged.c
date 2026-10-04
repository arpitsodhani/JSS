#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char swap_case_vowel(char c) {
    if (c == 'a') return 'C';
    if (c == 'e') return 'G';
    if (c == 'i') return 'K';
    if (c == 'o') return 'Q';
    if (c == 'u') return 'W';
    if (c == 'A') return 'c';
    if (c == 'E') return 'g';
    if (c == 'I') return 'k';
    if (c == 'O') return 'q';
    if (c == 'U') return 'w';
    if (islower(c)) return toupper(c);
    if (isupper(c)) return tolower(c);
    return c;
}

void encode(const char *message, char *result) {
    for (int i = 0; message[i]; i++) {
        result[i] = swap_case_vowel(message[i]);
    }
    result[strlen(message)] = 0;
}

void run(void) {

    char message[10000], result[10000];
    fgets(message, sizeof(message), stdin);
    message[strcspn(message, "\n")] = 0;
    encode(message, result);
    printf("%s\n", result);
}

int main() {
    run();
    return 0;
}
