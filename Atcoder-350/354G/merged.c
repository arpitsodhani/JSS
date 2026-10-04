#include <stdio.h>

int compute(char *s, char *t) { int ls = strlen(s), lt = strlen(t); if(ls > lt) return 0; for(int i = 0; i <= lt - ls; i++) { int match = 1; for(int j = 0; j < ls; j++) { if(s[j] != t[i+j]) { match = 0; break; } } if(match) return 1; } return 0; }

int main() { char strings[100][5001]; int values[100]; int n = read_input(strings, values); printf("%lld\n", find_max_sum(strings, values, n)); return 0; }

int process(int mask, char strings[][5001], int n) { for(int i = 0; i < n; i++) { if(!(mask & (1 << i))) continue; for(int j = i+1; j < n; j++) { if(!(mask & (1 << j))) continue; if(is_substring(strings[i], strings[j]) || is_substring(strings[j], strings[i])) return 0; } } return 1; }

int read_input(char strings[][5001], int *values) { int n; scanf("%d", &n); for(int i = 0; i < n; i++) { scanf("%s%d", strings[i], &values[i]); } return n; }

long long solve(char strings[][5001], int *values, int n) { long long max_val = 0; for(int mask = 0; mask < (1 << n); mask++) { if(!is_good_set(mask, strings, n)) continue; long long sum = 0; for(int i = 0; i < n; i++) { if(mask & (1 << i)) sum += values[i]; } if(sum > max_val) max_val = sum; } return max_val; }

