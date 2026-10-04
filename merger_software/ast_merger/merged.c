#include <stdio.h>

int sum_array(const int *a, int n) {
int sum = 0; for (int i = 0; i < n; i++) { sum += a[i]; } return sum;
}

int max_array(const int *a, int n) {
int m = a[0]; for (int i = 1; i < n; i++) { if (a[i] > m) m = a[i]; } return m;
}

int main(void) {
int a[3] = {1, 2, 3}; int s = sum_array(a, 3); int m = max_array(a, 3); printf("%d %d\n", s, m); return 0;
}
