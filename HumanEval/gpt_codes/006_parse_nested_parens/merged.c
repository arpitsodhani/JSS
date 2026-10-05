#include <stdio.h>

int main(void) {
    char input[1000];
    fgets(input, sizeof(input), stdin);
    int max_depth = 0;
    int current = 0;
    for (int i = 0; input[i] && input[i] != '\n'; i++) {
        if (input[i] == '(') {
            current++;
            if (current > max_depth) max_depth = current;
        } else if (input[i] == ')') {
            current--;
        } else if (input[i] == ' ' && current == 0) {
            if (max_depth > 0) printf("%d ", max_depth);
            max_depth = 0;
        }
    }
    if (max_depth > 0) printf("%d", max_depth);
    printf("\n");
    return 0;
}
