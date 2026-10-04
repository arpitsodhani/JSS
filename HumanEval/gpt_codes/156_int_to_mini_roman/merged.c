#include <stdio.h>
#include <string.h>

void int_to_roman(int num, char* result) {
    char* numerals[] = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
    int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    
    int idx = 0;
    for (int i = 0; i < 13; i++) {
        while (num >= values[i]) {
            strcpy(result + idx, numerals[i]);
            idx += strlen(numerals[i]);
            num -= values[i];
        }
    }
    result[idx] = '\0';
}

int main() {
    int number;
    scanf("%d", &number);
    
    char result[1000];
    int_to_roman(number, result);
    
    printf("%s\n", result);
    return 0;
}
