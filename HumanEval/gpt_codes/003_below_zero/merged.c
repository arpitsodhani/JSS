#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int ops[n];
    for (int i = 0; i < n; i++) scanf("%d", &ops[i]);
    
    int balance = 0;
    for (int i = 0; i < n; i++) {
        balance += ops[i];
        if (balance < 0) {
            printf("True\n");
            return 0;
        }
    }
    printf("False\n");
    return 0;
}

int check_negative(int *arr, int n) {
    int bal = 0;
    for (int i = 0; i < n; i++) {
        bal += arr[i];
        if (bal < 0) return 1;
    }
    return 0;
}
