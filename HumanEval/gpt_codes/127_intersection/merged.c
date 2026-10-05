#include <stdio.h>

int is_prime(int n) {
    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main() {
    int start1, end1, start2, end2;
    scanf("%d %d %d %d", &start1, &end1, &start2, &end2);
    
    int inter_start = (start1 > start2) ? start1 : start2;
    int inter_end = (end1 < end2) ? end1 : end2;
    
    if (inter_start > inter_end) {
        printf("NO\n");
        return 0;
    }
    
    int length = inter_end - inter_start;
    
    if (is_prime(length)) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }
    
    return 0;
}
