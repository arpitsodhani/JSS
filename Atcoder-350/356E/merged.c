#include <stdio.h>
#include <stdlib.h>

long long calculate_sum(long long arr[], int n) { qsort(arr, n, sizeof(long long), compare); long long sum = 0; for(int i = 0; i < n; i++) { for(int j = i + 1; j < n; j++) { sum += arr[j] / arr[i]; } } return sum; }

int compare(const void *a, const void *b) { long long x = *(long long*)a, y = *(long long*)b; return (x > y) - (x < y); }

int main() { long long a[1000005]; int n = read_input(a); printf("%lld\n", calculate_sum(a, n)); return 0; }

int read_input(long long arr[]) { int n; scanf("%d", &n); for(int i = 0; i < n; i++) scanf("%lld", &arr[i]); return n; }

