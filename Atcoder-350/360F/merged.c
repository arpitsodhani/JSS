#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void read_intervals(int *n, int **l, int **r) {
    scanf("%d", n);
    *l = malloc(*n * sizeof(int));
    *r = malloc(*n * sizeof(int));
    for (int i = 0; i < *n; i++) {
        scanf("%d %d", &(*l)[i], &(*r)[i]);
    }
}

int collect_candidate_points(int n, int *l, int *r, int *points) {
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        points[cnt++] = l[i];
        points[cnt++] = r[i];
        if (l[i] > 0) points[cnt++] = l[i] - 1;
        if (r[i] < 1000000000) points[cnt++] = r[i] + 1;
    }
    return cnt;
}

void find_best_interval(int n, int *l, int *r, int num_points, int *points, int *best_l, int *best_r) {
    int max_count = 0;
    *best_l = 0;
    *best_r = 1;
    for (int i = 0; i < num_points; i++) {
        for (int j = i + 1; j < num_points; j++) {
            int la = points[i], ra = points[j];
            if (la >= ra) continue;
            int count = 0;
            for (int k = 0; k < n; k++) {
                if ((l[k] < la && la < r[k] && r[k] < ra) || (la < l[k] && l[k] < ra && ra < r[k])) count++;
            }
            if (count > max_count || (count == max_count && (la < *best_l || (la == *best_l && ra < *best_r)))) {
                max_count = count;
                *best_l = la;
                *best_r = ra;
            }
        }
    }
}

int main() {
    int n, *l, *r;
    read_intervals(&n, &l, &r);
    int points[4000], num_points = collect_candidate_points(n, l, r, points);
    int best_l, best_r;
    find_best_interval(n, l, r, num_points, points, &best_l, &best_r);
    printf("%d %d\n", best_l, best_r);
    free(l);
    free(r);
    return 0;
}

