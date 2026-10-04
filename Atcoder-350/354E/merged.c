#include <stdio.h>

int read_input(int *a, int *b) { int n; scanf("%d", &n); for(int i = 0; i < n; i++) scanf("%d%d", &a[i], &b[i]); return n; }

int can_remove(int a1, int b1, int a2, int b2) { return a1 == a2 || b1 == b2; }

int solve(int mask, int *a, int *b, int n, int *memo) { if(memo[mask] != -1) return memo[mask]; for(int i = 0; i < n; i++) { if(!(mask & (1 << i))) continue; for(int j = i + 1; j < n; j++) { if(!(mask & (1 << j))) continue; if(can_remove(a[i], b[i], a[j], b[j])) { int newmask = mask ^ (1 << i) ^ (1 << j); if(!solve(newmask, a, b, n, memo)) { memo[mask] = 1; return 1; } } } } memo[mask] = 0; return 0; }

int main() { int a[18], b[18], memo[1<<18]; int n = read_input(a, b); for(int i = 0; i < (1 << n); i++) memo[i] = -1; printf("%s\n", solve((1 << n) - 1, a, b, n, memo) ? "Takahashi" : "Aoki"); return 0; }
