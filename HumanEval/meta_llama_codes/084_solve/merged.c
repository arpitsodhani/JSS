#include <stdio.h>

int main(void) {
    int number, sum = 0;
    if (scanf("%d", &number) != 1) return 1;
    do {
        sum += number % 10;
        number /= 10;
    } while (number > 0);
    char bits[32];
    int length = 0;
    do {
        bits[length++] = (char)('0' + sum % 2);
        sum /= 2;
    } while (sum > 0);
    while (length > 0) putchar(bits[--length]);
    putchar('\n');
    return 0;
}
