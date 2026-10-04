#include <stdio.h>

int check_balance(int *ops, int n) {
    int balance = 0;
    for (int i = 0; i < n; i++) {
        balance += ops[i];
        if (balance < 0) return 1;
    }
    return 0;
}

void run(void) {

    int n;
    scanf("%d", &n);
    int ops[n];
    for (int i = 0; i < n; i++) scanf("%d", &ops[i]);
    if (check_balance(ops, n)) {
        printf("True\n");
    } else {
        printf("False\n");
    }
}

int main() {
    run();
    return 0;
}

int goes_negative(int *operations, int count) {
    int total = 0;
    for (int i = 0; i < count; i++) {
        total += operations[i];
        if (total < 0) return 1;
    }
    return 0;
}

int goes_below(int *txn, int len) {
    int bal = 0;
    for (int i = 0; i < len; i++) {
        bal += txn[i];
        if (bal < 0) return 1;
    }
    return 0;
}

int hits_negative(int *entries, int num) {
    int running = 0;
    int idx = 0;
    while (idx < num) {
        running += entries[idx];
        if (running < 0) return 1;
        idx++;
    }
    return 0;
}

int account_negative(int *ops, int cnt) {
    int acc = 0;
    for (int k = 0; k < cnt; k++) {
        acc += ops[k];
        if (acc < 0) return 1;
    }
    return 0;
}
