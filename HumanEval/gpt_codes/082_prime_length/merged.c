#include <stdio.h>
#include <string.h>

int is_prime(int n) {
    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main() {
    char str[1000];
    fgets(str, 1000, stdin);
    
    int len = strlen(str);
    if (str[len-1] == '\n') len--;
    
    if (is_prime(len)) {
        printf("True\n");
    } else {
        printf("False\n");
    }
    
    return 0;
}
