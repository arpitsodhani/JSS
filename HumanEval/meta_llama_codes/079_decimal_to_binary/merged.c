#include <stdio.h>
#include <string.h>

void decimal_to_binary(int n, char *result) {
    sprintf(result, "db");
    char binary[100];
    int idx = 0;
    if (n == 0) {
        binary[idx++] = '0';
    } else {
        while (n > 0) {
            binary[idx++] = (n % 2) + '0';
            n /= 2;
        }
    }
    for (int i = idx - 1; i >= 0; i--) {
        int len = strlen(result);
        result[len] = binary[i];
        result[len + 1] = '\0';
    }
    strcat(result, "db");
}

int main(void) {
    int n;
    scanf("%d", &n);
    char result[200];
    decimal_to_binary(n, result);
    printf("%s\n", result);
    return 0;
}
