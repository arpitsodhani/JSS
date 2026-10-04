#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_input(int *n, int *t, int *p, int *l) {
    scanf("%d %d %d", n, t, p);
    for (int i = 0; i < *n; i++) scanf("%d", &l[i]);
}

int compute_days_needed(int n, int t, int p, int *l) {
    int count = 0;
    for (int i = 0; i < n; i++) if (l[i] >= t) count++;
    if (count >= p) return 0;
    int days = 0;
    while (count < p) {
        days++;
        count = 0;
        for (int i = 0; i < n; i++) if (l[i] + days >= t) count++;
    }
    return days;
}

int main() {
    int n, t, p, l[105];
    read_input(&n, &t, &p, l);
    printf("%d\n", compute_days_needed(n, t, p, l));
    return 0;
}
