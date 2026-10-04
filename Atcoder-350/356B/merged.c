#include <stdio.h>

int check_nutrients(int n, int m, int goals[], int nutrients[][105]) { for(int j = 0; j < m; j++) { int total = 0; for(int i = 0; i < n; i++) total += nutrients[i][j]; if(total < goals[j]) return 0; } return 1; }

int main() { int n, m, goals[105], nutrients[105][105]; read_input(&n, &m, goals, nutrients); printf("%s\n", check_nutrients(n, m, goals, nutrients) ? "Yes" : "No"); return 0; }

void read_input(int *n, int *m, int goals[], int nutrients[][105]) { scanf("%d%d", n, m); for(int i = 0; i < *m; i++) scanf("%d", &goals[i]); for(int i = 0; i < *n; i++) for(int j = 0; j < *m; j++) scanf("%d", &nutrients[i][j]); }

