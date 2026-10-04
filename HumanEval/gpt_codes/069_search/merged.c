#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int search(int* lst, int n) {
    int freq[1000] = {0};
    int max_val = 0;
    for (int i = 0; i < n; i++) {
        if (lst[i] > 0 && lst[i] < 1000) {
            freq[lst[i]]++;
            if (lst[i] > max_val) max_val = lst[i];
        }
    }
    for (int i = max_val; i >= 1; i--) {
        if (freq[i] >= i) return i;
    }
    return -1;
}

int main() {
    int n;
    scanf("%d", &n);
    int lst[n];
    for (int i = 0; i < n; i++) scanf("%d", &lst[i]);
    printf("%d\n", search(lst, n));
    return 0;
}

