#include <stdio.h>

int compute_sign_product(int* arr, int n, int* sum) {
    int prod = 1;
    *sum = 0;
    
    for (int i = 0; i < n; i++) {
        if (arr[i] == 0) {
            return 0;
        } else if (arr[i] < 0) {
            prod *= -1;
            *sum += -arr[i];
        } else {
            *sum += arr[i];
        }
    }
    
    return prod;
}

int main() {
    int n;
    scanf("%d", &n);
    
    if (n == 0) {
        printf("None\n");
        return 0;
    }
    
    int arr[1000];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    
    int sum;
    int prod = compute_sign_product(arr, n, &sum);
    
    printf("%d\n", prod * sum);
    return 0;
}
