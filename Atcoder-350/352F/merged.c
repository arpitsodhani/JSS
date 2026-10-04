#include <stdio.h>

void read_input(int *n, int *m, int edges[][3]) { scanf("%d%d", n, m); for(int i = 0; i < *m; i++) scanf("%d%d%d", &edges[i][0], &edges[i][1], &edges[i][2]); }

int check_valid(int rank[], int n, int edges[][3], int m) { for(int i = 0; i < m; i++) { if(rank[edges[i][0]] - rank[edges[i][1]] != edges[i][2]) return 0; } return 1; }

void permute(int arr[], int l, int r, int edges[][3], int m, int results[]) { if(l == r) { if(check_valid(arr, r+1, edges, m)) { for(int i = 0; i <= r; i++) { if(results[i] == -1) results[i] = arr[i]; else if(results[i] != arr[i]) results[i] = -2; } } return; } for(int i = l; i <= r; i++) { int t = arr[l]; arr[l] = arr[i]; arr[i] = t; permute(arr, l+1, r, edges, m, results); t = arr[l]; arr[l] = arr[i]; arr[i] = t; } }

void solve(int n, int edges[][3], int m) { int arr[20], results[20]; for(int i = 0; i < n; i++) { arr[i] = i + 1; results[i] = -1; } permute(arr, 0, n-1, edges, m, results); for(int i = 0; i < n; i++) printf("%d\n", results[i] == -2 || results[i] == -1 ? -1 : results[i]); }

int main() { int n, m, edges[120][3]; read_input(&n, &m, edges); solve(n, edges, m); return 0; }
