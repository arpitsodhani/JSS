#include <stdio.h>

void read_stands(int n, int m, int stands[]) { for(int i = 0; i < n; i++) { stands[i] = 0; char s[15]; scanf("%s", s); for(int j = 0; j < m; j++) { if(s[j] == 'o') stands[i] |= (1 << j); } } }

int find_minimum_stands(int n, int m, int stands[]) { int all_flavors = (1 << m) - 1; int min_count = n + 1; for(int mask = 0; mask < (1 << n); mask++) { int covered = 0; int count = 0; for(int i = 0; i < n; i++) { if(mask & (1 << i)) { covered |= stands[i]; count++; } } if(covered == all_flavors && count < min_count) { min_count = count; } } return min_count; }

int main() { int n, m; scanf("%d%d", &n, &m); int stands[15]; read_stands(n, m, stands); printf("%d\n", find_minimum_stands(n, m, stands)); return 0; }
