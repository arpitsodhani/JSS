#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int choose_num(int x, int y) {
    if (y < x) return -1;
    if (y % 2 == 0) return y;
    if (y - 1 >= x) return y - 1;
    return -1;
}

void run(void) {

    int x, y;
    scanf("%d %d", &x, &y);
    printf("%d\n", choose_num(x, y));
}

int main() {
    run();
    return 0;
}
