#include <stdio.h>
#include <string.h>

int main(void) {
    char brackets[1000];
    fgets(brackets, sizeof(brackets), stdin);
    brackets[strcspn(brackets, "\n")] = 0;
    int depth = 0;
    for (int i = 0; brackets[i]; i++) {
        if (brackets[i] == '(') depth++;
        else if (brackets[i] == ')') depth--;
        if (depth < 0) {
            printf("False\n");
            return 0;
        }
    }
    printf("%s\n", depth == 0 ? "True" : "False");
    return 0;
}
