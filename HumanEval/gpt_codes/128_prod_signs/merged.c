#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int prod_signs(int n, int arr[]) {
    if (n == 0) return -32768;
    
    int prod = 1;
    int sum = 0;
    
    for (int i = 0; i < n; i++) {
        if (arr[i] == 0) return 0;
        
        if (arr[i] < 0) {
            prod *= -1;
            sum += -arr[i];
        } else {
            sum += arr[i];
        }
    }
    
    return prod * sum;
}

int main() {
    int n;
    scanf("%d", &n);
    if (n == 0) {
        printf("-32768\n");
        return 0;
    }
    int arr[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    printf("%d\n", prod_signs(n, arr));
    return 0;
}
