#include <stdio.h>

int read_input(int n, int times[]) { int a; scanf("%d%d", &n, &a); for(int i = 0; i < n; i++) scanf("%d", &times[i]); return a; }

void calculate_service_times(int n, int times[], int a, int results[]) { int finish = 0; for(int i = 0; i < n; i++) { if(times[i] > finish) finish = times[i]; finish += a; results[i] = finish; } }

void print_results(int n, int results[]) { for(int i = 0; i < n; i++) printf("%d\n", results[i]); }

int main() { int n, times[105], results[105]; int a = read_input(n, times); calculate_service_times(n, times, a, results); print_results(n, results); return 0; }
