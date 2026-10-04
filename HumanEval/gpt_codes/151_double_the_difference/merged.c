#include <stdio.h>

int compute_sum_odd_squares(double* lst, int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        if (lst[i] > 0 && lst[i] == (int)lst[i]) {
            int val = (int)lst[i];
            if (val % 2 == 1) {
                sum += val * val;
            }
        }
    }
    return sum;
}

int main() {
    int n;
    scanf("%d", &n);
    
    double lst[1000];
    for (int i = 0; i < n; i++) {
        scanf("%lf", &lst[i]);
    }
    
    printf("%d\n", compute_sum_odd_squares(lst, n));
    return 0;
}
