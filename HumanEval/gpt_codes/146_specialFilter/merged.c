#include <stdio.h>

int check_special(int num) {
    if (num < 10) return 0;
    
    int first = -1, last = -1;
    int temp = num < 0 ? -num : num;
    
    last = temp % 10;
    while (temp > 0) {
        first = temp % 10;
        temp /= 10;
    }
    
    return (first % 2 == 1 && last % 2 == 1);
}

int main() {
    int n;
    scanf("%d", &n);
    
    int nums[1000];
    for (int i = 0; i < n; i++) {
        scanf("%d", &nums[i]);
    }
    
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (nums[i] > 10 && check_special(nums[i])) {
            count++;
        }
    }
    
    printf("%d\n", count);
    return 0;
}
