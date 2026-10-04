#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <math.h>

int check_item_fits_capacity(int item_weight, int remaining_capacity) {
    return item_weight <= remaining_capacity;
}

int select_maximum_value_item(int n, int *weights, int *values, int capacity, int *selected) {
    int best_idx = -1;
    int best_value = 0;
    for (int i = 0; i < n; i++) {
        if (!selected[i] && check_item_fits_capacity(weights[i], capacity)) {
            if (values[i] > best_value) {
                best_value = values[i];
                best_idx = i;
            }
        }
    }
    return best_idx;
}

int compute_knapsack_greedy(int n, int *weights, int *values, int capacity) {
    int selected[105] = {0};
    int total_value = 0;
    int remaining = capacity;
    
    while (1) {
        int idx = select_maximum_value_item(n, weights, values, remaining, selected);
        if (idx == -1) break;
        selected[idx] = 1;
        total_value += values[idx];
        remaining -= weights[idx];
    }
    return total_value;
}

int main() {
    int n, capacity, weights[105], values[105];
    scanf("%d %d", &n, &capacity);
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &weights[i], &values[i]);
    }
    printf("%d\n", compute_knapsack_greedy(n, weights, values, capacity));
    return 0;
}