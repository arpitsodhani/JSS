#include <stdio.h>

void rolling_max(int *arr, int n) {
    int max_val = arr[0];
    for (int i = 0; i < n; i++) {
        if (arr[i] > max_val) max_val = arr[i];
        printf("%d", max_val);
        if (i < n - 1) printf(" ");
    }
    printf("\n");
}

int main(void) {
    int n;
    scanf("%d", &n);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    rolling_max(arr, n);
    return 0;
}

void compute_rolling(int *data, int size) {
    int current_max = data[0];
    for (int i = 0; i < size; i++) {
        if (data[i] > current_max) current_max = data[i];
        printf("%d", current_max);
        if (i < size - 1) printf(" ");
    }
    printf("\n");
}

void running_peak(int *arr, int n) {
    int peak = arr[0];
    for (int i = 0; i < n; i++) {
        if (arr[i] > peak) peak = arr[i];
        printf("%d", peak);
        if (i < n - 1) printf(" ");
    }
    printf("\n");
}

void print_max_so_far(int *vals, int sz) {
    int best = vals[0];
    int i = 0;
    while (i < sz) {
        if (vals[i] > best) best = vals[i];
        if (i > 0) printf(" ");
        printf("%d", best);
        i++;
    }
    printf("\n");
}

void seq_maximum(int *data, int len) {
    int mx = data[0];
    for (int k = 0; k < len; k++) {
        if (data[k] > mx) mx = data[k];
        printf("%d", mx);
        if (k < len - 1) printf(" ");
    }
    printf("\n");
}
