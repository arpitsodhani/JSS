#include <stdio.h>

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int parse_and_multiply(char* x, char* n) {
    int x_num, x_den, n_num, n_den;
    sscanf(x, "%d/%d", &x_num, &x_den);
    sscanf(n, "%d/%d", &n_num, &n_den);
    
    int result_num = x_num * n_num;
    int result_den = x_den * n_den;
    
    int g = gcd(result_num < 0 ? -result_num : result_num, result_den);
    result_num /= g;
    result_den /= g;
    
    return (result_den == 1 && result_num == result_den);
}

int main() {
    char x[100], n[100];
    scanf("%s %s", x, n);
    
    if (parse_and_multiply(x, n)) {
        printf("True\n");
    } else {
        printf("False\n");
    }
    
    return 0;
}
