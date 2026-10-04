#include <stdio.h>

int main() { int n, l, r; read_input(&n, &l, &r); int arr[105]; for(int i = 1; i <= n; i++) arr[i] = i; reverse_range(arr, l, r); print_sequence(arr, n); return 0; }

void print_sequence(int arr[], int n) { for(int i = 1; i <= n; i++) printf("%d%c", arr[i], i == n ? '\n' : ' '); }

void read_input(int *n, int *l, int *r) { scanf("%d%d%d", n, l, r); }

void reverse_range(int arr[], int l, int r) { while(l < r) { int tmp = arr[l]; arr[l] = arr[r]; arr[r] = tmp; l++; r--; } }

