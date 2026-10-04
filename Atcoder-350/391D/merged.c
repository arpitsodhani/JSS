#include <stdio.h>
#include <stdlib.h>

void read_input(int *n, int arr[]) {
    scanf("%d", n);
    for (int i = 0; i < *n; i++) {
        scanf("%d", &arr[i]);
    }
}

int compute_sum(int n, int arr[]) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return sum;
}

void print_result(int result) {
    printf("%d\n", result);
}

int main() {
    int n;
    int arr[1000];
    read_input(&n, arr);
    int result = compute_sum(n, arr);
    print_result(result);
    return 0;
}

