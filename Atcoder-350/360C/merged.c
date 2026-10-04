#include <stdio.h>

int read_items(int a[], int w[]) { int n; scanf("%d", &n); for(int i = 0; i < n; i++) scanf("%d", &a[i]); for(int i = 0; i < n; i++) scanf("%d", &w[i]); return n; }

void find_box_weights(int n, int a[], int w[], int box_max[]) { for(int i = 1; i <= n; i++) box_max[i] = 0; for(int i = 0; i < n; i++) { int box = a[i]; if(w[i] > box_max[box]) box_max[box] = w[i]; } }

long long compute_minimum_cost(int n, int a[], int w[], int box_max[]) { long long total = 0; for(int i = 0; i < n; i++) total += w[i]; for(int i = 1; i <= n; i++) total -= box_max[i]; return total; }

int main() { int a[100005], w[100005], box_max[100005]; int n = read_items(a, w); find_box_weights(n, a, w, box_max); printf("%lld\n", compute_minimum_cost(n, a, w, box_max)); return 0; }
