#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void decimal_to_binary(int decimal, char* result) {
    if (decimal == 0) {
        strcpy(result, "db0db");
        return;
    }
    char binary[100];
    int idx = 0;
    int num = decimal;
    while (num > 0) {
        binary[idx++] = '0' + (num % 2);
        num /= 2;
    }
    strcpy(result, "db");
    for (int i = idx - 1; i >= 0; i--) {
        int len = strlen(result);
        result[len] = binary[i];
        result[len + 1] = '\0';
    }
    strcat(result, "db");
}

int main() {
    int decimal;
    scanf("%d", &decimal);
    char result[100];
    decimal_to_binary(decimal, result);
    printf("%s\n", result);
    return 0;
}

