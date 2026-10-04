#include <stdio.h>
#include <string.h>

void xor_strings(char *a, char *b) {
    int len = strlen(a);
    for (int i = 0; i < len; i++) {
        printf("%c", (a[i] == b[i]) ? '0' : '1');
    }
    printf("\n");
}

void run(void) {

    char a[1000], b[1000];
    scanf("%s %s", a, b);
    xor_strings(a, b);
}

int main() {
    run();
    return 0;
}

void binary_xor(char *str1, char *str2) {
    int length = strlen(str1);
    for (int i = 0; i < length; i++) {
        printf("%c", (str1[i] != str2[i]) ? '1' : '0');
    }
    printf("\n");
}

void bitwise_str_xor(char *x, char *y) {
    int n = strlen(x);
    for (int i = 0; i < n; i++)
        printf("%c", (x[i] == y[i]) ? '0' : '1');
    printf("\n");
}

void char_xor(char *p, char *q) {
    int sz = strlen(p);
    int i = 0;
    while (i < sz) {
        printf("%c", (p[i] != q[i]) ? '1' : '0');
        i++;
    }
    printf("\n");
}

void xor_bits(char *u, char *v) {
    for (int k = 0; u[k]; k++)
        printf("%c", (u[k] == v[k]) ? '0' : '1');
    printf("\n");
}
