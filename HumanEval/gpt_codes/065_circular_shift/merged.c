#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void circular_shift(int x, int shift, char* result) {
    char num[20];
    sprintf(num, "%d", x);
    int len = strlen(num);
    if (shift > len) {
        strcpy(result, num);
        int i = 0, j = len - 1;
        while (i < j) {
            char temp = result[i];
            result[i] = result[j];
            result[j] = temp;
            i++; j--;
        }
        return;
    }
    shift = shift % len;
    for (int i = 0; i < len; i++) {
        result[i] = num[(len - shift + i) % len];
    }
    result[len] = '\0';
}

int main() {
    int x, shift;
    scanf("%d %d", &x, &shift);
    char result[20];
    circular_shift(x, shift, result);
    printf("%s\n", result);
    return 0;
}

