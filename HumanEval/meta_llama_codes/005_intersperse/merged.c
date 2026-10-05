#include <stdio.h>

void intersperse_print(int *arr, int n, int delim) {
    for (int i = 0; i < n; i++) {
        printf("%d", arr[i]);
        if (i < n - 1) printf(" %d ", delim);
    }
    printf("\n");
}

int main(void) {
    int n, delim;
    scanf("%d %d", &n, &delim);
    int arr[n];
    for (int i = 0; i < n; i++) scanf("%d", &arr[i]);
    intersperse_print(arr, n, delim);
    return 0;
}
