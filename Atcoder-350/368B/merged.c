#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <math.h>

void extract_window_values(int *array, int center, int window_size, int *window) {
    int half = window_size / 2;
    for (int i = 0; i < window_size; i++) {
        window[i] = array[center - half + i];
    }
}

int find_median_value(int *window, int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = i + 1; j < size; j++) {
            if (window[j] < window[i]) {
                int tmp = window[i];
                window[i] = window[j];
                window[j] = tmp;
            }
        }
    }
    return window[size / 2];
}

void apply_median_filter(int n, int *input, int *output, int window_size) {
    int half = window_size / 2;
    for (int i = half; i < n - half; i++) {
        int window[105];
        extract_window_values(input, i, window_size, window);
        output[i] = find_median_value(window, window_size);
    }
}

int main() {
    int n, window_size, input[10005], output[10005];
    scanf("%d %d", &n, &window_size);
    for (int i = 0; i < n; i++) scanf("%d", &input[i]);
    apply_median_filter(n, input, output, window_size);
    int half = window_size / 2;
    for (int i = half; i < n - half; i++) {
        printf("%d ", output[i]);
    }
    return 0;
}