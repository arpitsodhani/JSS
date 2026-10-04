#include <stdio.h>

int count_valid_assignments(int n, int k, int m, int tests[][20], int outcomes[], int counts[]) { int valid = 0; for(int mask = 0; mask < (1 << n); mask++) { int ok = 1; for(int i = 0; i < m && ok; i++) { int real_count = 0; for(int j = 0; j < counts[i]; j++) if(mask & (1 << (tests[i][j] - 1))) real_count++; ok = ((real_count >= k) == outcomes[i]); } if(ok) valid++; } return valid; }

int main() { int n, k, tests[105][20], outcomes[105], counts[105]; int m = read_input(&n, &k, tests, outcomes, counts); printf("%d\n", count_valid_assignments(n, k, m, tests, outcomes, counts)); return 0; }

int read_input(int *n, int *k, int tests[][20], int outcomes[], int counts[]) { int m; scanf("%d%d%d", n, k, &m); for(int i = 0; i < m; i++) { int c; char r; scanf("%d", &c); counts[i] = c; for(int j = 0; j < c; j++) scanf("%d", &tests[i][j]); scanf(" %c", &r); outcomes[i] = (r == 'o'); } return m; }

