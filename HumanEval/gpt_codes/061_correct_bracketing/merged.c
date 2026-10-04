#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int correct_bracketing(char* brackets) {
    int depth = 0;
    for (int i = 0; brackets[i]; i++) {
        if (brackets[i] == '(') depth++;
        else if (brackets[i] == ')') depth--;
        if (depth < 0) return 0;
    }
    return depth == 0;
}

int main() {
    char brackets[1000];
    if (fgets(brackets, sizeof(brackets), stdin)) {
        brackets[strcspn(brackets, "\n")] = 0;
    } else {
        brackets[0] = 0;
    }
    printf("%s\n", correct_bracketing(brackets) ? "True" : "False");
    return 0;
}

