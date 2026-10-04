#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void read_ranges(int *n, long long *l, long long *r) {
    scanf("%d", n);
    for (int i = 0; i < *n; i++) {
        scanf("%lld %lld", &l[i], &r[i]);
    }
}

int check_feasibility(int n, long long *l, long long *r) {
    long long min_sum = 0, max_sum = 0;
    for (int i = 0; i < n; i++) {
        min_sum += l[i];
        max_sum += r[i];
    }
    return (min_sum <= 0 && max_sum >= 0) ? 1 : 0;
}

void construct_sequence(int n, long long *l, long long *r, long long *x) {
    long long sum = 0;
    for (int i = 0; i < n; i++) {
        x[i] = l[i];
        sum += l[i];
    }
    for (int i = 0; i < n && sum < 0; i++) {
        long long add = (r[i] - l[i] < -sum) ? (r[i] - l[i]) : -sum;
        x[i] += add;
        sum += add;
    }
}

int main() {
    int n;
    long long l[200005], r[200005], x[200005];
    read_ranges(&n, l, r);
    if (check_feasibility(n, l, r)) {
        printf("Yes\n");
        construct_sequence(n, l, r, x);
        for (int i = 0; i < n; i++) printf("%lld%c", x[i], i == n - 1 ? '\n' : ' ');
    } else {
        printf("No\n");
    }
    return 0;
}

