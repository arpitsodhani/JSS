#include <stdio.h>

int is_prime(int n) {
    if (n < 2) return 0;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int largest_prime_digit(int* arr, int n) {
    int max_prime = -1;
    for (int i = 0; i < n; i++) {
        if (is_prime(arr[i]) && arr[i] > max_prime) {
            max_prime = arr[i];
        }
    }
    return max_prime;
}

int main() {
    int n;
    scanf("%d", &n);
    
    int arr[1000];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    
    int max_prime = largest_prime_digit(arr, n);
    
    if (max_prime == -1) {
        printf("0\n");
    } else {
        int sum = 0;
        while (max_prime > 0) {
            sum += max_prime % 10;
            max_prime /= 10;
        }
        printf("%d\n", sum);
    }
    
    return 0;
}
