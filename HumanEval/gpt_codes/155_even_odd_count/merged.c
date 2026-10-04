#include <stdio.h>
#include <stdlib.h>

int main() {
    int param_count;
    scanf("%d", &param_count);
    
    int num;
    scanf("%d", &num);
    
    if (num < 0) num = -num;
    
    int even = 0, odd = 0;
    
    if (num == 0) {
        even = 1;
    } else {
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                even++;
            } else {
                odd++;
            }
            num /= 10;
        }
    }
    
    printf("(%d, %d)\n", even, odd);
    return 0;
}
