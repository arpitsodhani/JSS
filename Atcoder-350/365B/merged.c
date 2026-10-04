#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int update_current_maximum(int current_max, int element) {
    int new_max = current_max + element;
    return new_max > element ? new_max : element;
}

int update_global_maximum(int global_max, int current_max) {
    return current_max > global_max ? current_max : global_max;
}

int track_maximum_subarray_sum(int n, int *array) {
    int current_max = array[0];
    int global_max = array[0];
    for (int i = 1; i < n; i++) {
        current_max = update_current_maximum(current_max, array[i]);
        global_max = update_global_maximum(global_max, current_max);
    }
    return global_max;
}

int main() {
    int n, array[100005];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &array[i]);
    printf("%d\n", track_maximum_subarray_sum(n, array));
    return 0;
}