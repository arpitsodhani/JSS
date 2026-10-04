#include <stdio.h>

int add(int x, int y) {
    return x + y;
}

int main() {
    int x, y;
    scanf("%d %d", &x, &y);
    printf("%d\n", add(x, y));
    return 0;
}

int sum_two(int x, int y) {
    return x + y;
}

int add_vals(int a, int b) {
    int res=a;
    res+=b;
    return res;
}

int plus(int m, int n) {
    return m + n;
}

int integer_add(int p, int q) {
    return p + q;
}
