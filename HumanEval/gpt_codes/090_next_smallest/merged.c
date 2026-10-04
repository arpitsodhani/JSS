#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare_int(const void *a, const void *b) {
    return *(int*)a - *(int*)b;
}

int next_smallest(int n, int lst[]) {
    if (n < 2) return -1;
    qsort(lst, n, sizeof(int), compare_int);
    for (int i = 1; i < n; i++) {
        if (lst[i] != lst[0]) {
            return lst[i];
        }
    }
    return -1;
}

void run(void) {

    int n;
    scanf("%d", &n);
    int lst[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &lst[i]);
    }
    int result = next_smallest(n, lst);
    if (result == -1) {
        printf("None\n");
    } else {
        printf("%d\n", result);
    }
}

int main() {
    run();
    return 0;
}
