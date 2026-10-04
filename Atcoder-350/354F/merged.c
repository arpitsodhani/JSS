#include <stdio.h>

int read_input(int *a) { int n; scanf("%d", &n); for(int i = 0; i < n; i++) scanf("%d", &a[i]); return n; }

int lis_len(int *a, int n) { int dp[200000], len = 0; for(int i = 0; i < n; i++) { int pos = 0; while(pos < len && dp[pos] < a[i]) pos++; dp[pos] = a[i]; if(pos == len) len++; } return len; }

int in_lis(int *a, int n, int idx, int target_len) { int left[200000], right[200000]; for(int i = 0; i <= idx; i++) left[i] = 1; for(int i = 0; i < idx; i++) for(int j = i + 1; j <= idx; j++) if(a[i] < a[j] && left[i] + 1 > left[j]) left[j] = left[i] + 1; for(int i = n - 1; i >= idx; i--) right[i] = 1; for(int i = n - 1; i > idx; i--) for(int j = i - 1; j >= idx; j--) if(a[j] < a[i] && right[i] + 1 > right[j]) right[j] = right[i] + 1; return left[idx] + right[idx] - 1 == target_len; }

void output(int *a, int n) { int len = lis_len(a, n); for(int i = 0; i < n; i++) { if(in_lis(a, n, i, len)) printf("%d ", i + 1); } printf("\n"); }

int main() { int t; scanf("%d", &t); while(t--) { int a[200000]; int n = read_input(a); output(a, n); } return 0; }
