#include <stdio.h>

int read_input(int *arr) { int n; scanf("%d", &n); for(int i = 0; i < n; i++) scanf("%d", &arr[i]); return n; }

long long compute_mod(long long x, long long y) { long long sum = x + y; if(sum >= 100000000LL) sum -= 100000000LL; return sum; }

long long count_pairs(int *arr, int n) { long long result = 0; for(int i = 0; i < n - 1; i++) { for(int j = i + 1; j < n; j++) { result += compute_mod(arr[i], arr[j]); } } return result; }

int main() { int arr[300000]; int n = read_input(arr); printf("%lld\n", count_pairs(arr, n)); return 0; }
