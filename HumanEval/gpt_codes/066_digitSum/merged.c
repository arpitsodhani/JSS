#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int digitSum(char* s) {
    int sum = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] >= 'A' && s[i] <= 'Z') {
            sum += s[i];
        }
    }
    return sum;
}

int main() {
    char s[1000];
    if (fgets(s, sizeof(s), stdin)) {
        s[strcspn(s, "\n")] = 0;
    } else {
        s[0] = 0;
    }
    printf("%d\n", digitSum(s));
    return 0;
}

