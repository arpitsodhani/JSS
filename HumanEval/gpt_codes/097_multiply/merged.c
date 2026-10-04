#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int multiply(int a, int b) {
    a = abs(a) % 10;
    b = abs(b) % 10;
    return a * b;
}

void run(void) {

    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d\n", multiply(a, b));
}

int main() {
    run();
    return 0;
}
