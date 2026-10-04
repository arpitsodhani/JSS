#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int digits(int n) {
    int product = 1;
    int has_odd = 0;
    
    while (n > 0) {
        int digit = n % 10;
        if (digit % 2 == 1) {
            product *= digit;
            has_odd = 1;
        }
        n /= 10;
    }
    
    return has_odd ? product : 0;
}

int main() {
    int n;
    scanf("%d", &n);
    printf("%d\n", digits(n));
    return 0;
}
