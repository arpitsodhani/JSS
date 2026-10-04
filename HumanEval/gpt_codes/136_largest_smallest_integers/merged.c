#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

void largest_smallest_integers(int n, int lst[], int *a, int *b) {
    *a = 0;
    *b = 0;
    
    int max_neg = -1000000;
    int min_pos = 1000000;
    int has_neg = 0, has_pos = 0;
    
    for (int i = 0; i < n; i++) {
        if (lst[i] < 0) {
            has_neg = 1;
            if (lst[i] > max_neg) {
                max_neg = lst[i];
            }
        } else if (lst[i] > 0) {
            has_pos = 1;
            if (lst[i] < min_pos) {
                min_pos = lst[i];
            }
        }
    }
    
    if (has_neg) *a = max_neg;
    if (has_pos) *b = min_pos;
}

int main() {
    int n;
    scanf("%d", &n);
    int lst[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &lst[i]);
    }
    int a, b;
    largest_smallest_integers(n, lst, &a, &b);
    printf("(%d, %d)\n", a, b);
    return 0;
}
