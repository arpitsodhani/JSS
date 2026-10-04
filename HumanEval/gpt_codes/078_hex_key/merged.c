#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int hex_key(char* num) {
    int count = 0;
    for (int i = 0; num[i]; i++) {
        char c = num[i];
        if (c == '2' || c == '3' || c == '5' || c == '7' || c == 'B' || c == 'D') {
            count++;
        }
    }
    return count;
}

int main() {
    char num[1000];
    if (fgets(num, sizeof(num), stdin)) {
        num[strcspn(num, "\n")] = 0;
    } else {
        num[0] = 0;
    }
    printf("%d\n", hex_key(num));
    return 0;
}

