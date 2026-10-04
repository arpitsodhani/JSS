#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

long long minSubArraySum(int n, long long nums[]) {
    long long min_sum = nums[0];
    long long current_sum = nums[0];
    
    for (int i = 1; i < n; i++) {
        current_sum = (nums[i] < current_sum + nums[i]) ? nums[i] : current_sum + nums[i];
        if (current_sum < min_sum) {
            min_sum = current_sum;
        }
    }
    
    return min_sum;
}

int main() {
    int n;
    scanf("%d", &n);
    long long nums[n];
    for (int i = 0; i < n; i++) {
        scanf("%lld", &nums[i]);
    }
    printf("%lld\n", minSubArraySum(n, nums));
    return 0;
}

