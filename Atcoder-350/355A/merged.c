#include <stdio.h>

int main() { int a, b; read_input(&a, &b); int ans = find_culprit(a, b); printf("%d\n", ans); return 0; }

void read_input(int *a, int *b) { scanf("%d%d", a, b); }

int solve(int a, int b) { int cnt = 0, culprit = 0; for(int i = 1; i <= 3; i++) { if(i != a && i != b) { cnt++; culprit = i; } } return cnt == 1 ? culprit : -1; }

