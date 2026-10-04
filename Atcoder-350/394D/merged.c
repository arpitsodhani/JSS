#include <stdio.h>
#include <stdlib.h>

void read_input(int *n, int arr[]) {
    scanf("%d", n);
    for (int i = 0; i < *n; i++) {
        scanf("%d", &arr[i]);
    }
}

int find_maximum(int n, int arr[]) {
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

void print_result(int max) {
    printf("%d\n", max);
}

int main() {
    int n;
    int arr[1000];
    read_input(&n, arr);
    int max = find_maximum(n, arr);
    print_result(max);
    return 0;
}

