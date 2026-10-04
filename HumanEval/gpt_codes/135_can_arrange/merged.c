#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int can_arrange(int n, int arr[]) {
    int max_index = -1;
    
    for (int i = 0; i < n; i++) {
        if (arr[i] <= i) {
            max_index = i;
        }
    }
    
    return max_index;
}

int main() {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    printf("%d\n", can_arrange(n, arr));
    return 0;
}
