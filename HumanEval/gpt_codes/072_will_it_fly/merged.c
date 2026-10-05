#include <stdio.h>

int will_it_fly(int *arr, int n, int w) {
    int is_palindrome = 1;
    for (int i = 0; i < n / 2; i++) {
        if (arr[i] != arr[n - 1 - i]) {
            is_palindrome = 0;
            break;
        }
    }
    if (!is_palindrome) return 0;
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return sum <= w;
}

int main(void) {
    int n, w;
    scanf("%d %d", &n, &w);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    if (will_it_fly(arr, n, w)) {
        printf("True\n");
    } else {
        printf("False\n");
    }
    return 0;
}
