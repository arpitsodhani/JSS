#include <stdio.h>
#include <string.h>

void convert_base(int num, int base, char* result) {
    if (num == 0) {
        result[0] = '0';
        result[1] = '\0';
        return;
    }
    
    char temp[100];
    int i = 0;
    while (num > 0) {
        temp[i++] = '0' + (num % base);
        num /= base;
    }
    
    for (int j = 0; j < i; j++) {
        result[j] = temp[i - 1 - j];
    }
    result[i] = '\0';
}

int main() {
    int num, base;
    scanf("%d %d", &num, &base);
    
    char result[100];
    convert_base(num, base, result);
    
    printf("%s\n", result);
    return 0;
}
