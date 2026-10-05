#include <stdio.h>

int count_sevens(int n) {
    int count = 0;
    while (n > 0) {
        if (n % 10 == 7) count++;
        n /= 10;
    }
    return count;
}

int main() {
    int n;
    scanf("%d", &n);
    
    int total = 0;
    for (int i = 1; i < n; i++) {
        if (i % 11 == 0 || i % 13 == 0) {
            total += count_sevens(i);
        }
    }
    
    printf("%d\n", total);
    return 0;
}
