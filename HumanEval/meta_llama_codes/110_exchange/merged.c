#include <stdio.h>

int can_exchange(int *arr1, int n1, int *arr2, int n2) {
    int odd1 = 0, even2 = 0;
    for (int i = 0; i < n1; i++) {
        if (arr1[i] % 2 == 1) odd1++;
    }
    for (int i = 0; i < n2; i++) {
        if (arr2[i] % 2 == 0) even2++;
    }
    return odd1 <= even2;
}

int main(void) {
    int n1, n2;
    scanf("%d", &n1);
    int arr1[n1];
    for (int i = 0; i < n1; i++) scanf("%d", &arr1[i]);
    scanf("%d", &n2);
    int arr2[n2];
    for (int i = 0; i < n2; i++) scanf("%d", &arr2[i]);
    if (can_exchange(arr1, n1, arr2, n2)) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }
    return 0;
}
