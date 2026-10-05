#include <stdio.h>
#include <string.h>

void circular_shift(char *num_str, int shift, char *result) {
    int len = strlen(num_str);
    if (shift > len) {
        for (int i = 0; i < len; i++) {
            result[i] = num_str[len - 1 - i];
        }
        result[len] = '\0';
    } else {
        for (int i = 0; i < len; i++) {
            result[i] = num_str[(i - shift + len) % len];
        }
        result[len] = '\0';
    }
}

int main(void) {
    int num, shift;
    scanf("%d %d", &num, &shift);
    char num_str[50];
    sprintf(num_str, "%d", num);
    char result[50];
    circular_shift(num_str, shift, result);
    printf("%s\n", result);
    return 0;
}
