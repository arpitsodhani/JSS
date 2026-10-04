#include <stdio.h>

void compute(int a[], int n, int b[], int m, int c[], int *from_a[]) { int i = 0, j = 0, k = 0; while(i < n && j < m) { if(a[i] < b[j]) { c[k] = a[i]; from_a[k++] = 1; i++; } else { c[k] = b[j]; from_a[k++] = 0; j++; } } while(i < n) { c[k] = a[i++]; from_a[k++] = 1; } while(j < m) { c[k] = b[j++]; from_a[k++] = 0; } }

int main() { int n, m, a[100], b[100], c[200], from_a[200]; read_input(&n, &m, a, b); merge_sequences(a, n, b, m, c, from_a); printf("%s\n", check_consecutive(from_a, n+m) ? "Yes" : "No"); return 0; }

void read_input(int *n, int *m, int a[], int b[]) { scanf("%d%d", n, m); for(int i = 0; i < *n; i++) scanf("%d", &a[i]); for(int j = 0; j < *m; j++) scanf("%d", &b[j]); }

int solve(int from_a[], int len) { for(int i = 0; i < len - 1; i++) { if(from_a[i] && from_a[i+1]) return 1; } return 0; }

