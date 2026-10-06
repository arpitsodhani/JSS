#include <stdio.h>

void find_largest_smallest(int* arr, int n, int* largest_neg, int* smallest_pos) {
    *largest_neg = 0;
    *smallest_pos = 0;
    int has_neg = 0, has_pos = 0;
    
    for (int i = 0; i < n; i++) {
        if (arr[i] < 0) {
            if (!has_neg || arr[i] > *largest_neg) {
                *largest_neg = arr[i];
                has_neg = 1;
            }
        } else if (arr[i] > 0) {
            if (!has_pos || arr[i] < *smallest_pos) {
                *smallest_pos = arr[i];
                has_pos = 1;
            }
        }
    }
    
    if (!has_neg) *largest_neg = 0;
    if (!has_pos) *smallest_pos = 0;
}

int main() {
    int n;
    scanf("%d", &n);
    
    int arr[1000];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    
    int largest_neg, smallest_pos;
    find_largest_smallest(arr, n, &largest_neg, &smallest_pos);
    
    if (largest_neg) printf("%d\n", largest_neg); else printf("None\n");
    if (smallest_pos) printf("%d\n", smallest_pos); else printf("None\n");
    return 0;
}
