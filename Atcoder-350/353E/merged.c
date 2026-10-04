#include <stdio.h>

int read_input(char s[][300001]) { int n; scanf("%d", &n); for(int i = 0; i < n; i++) scanf("%s", s[i]); return n; }

int lcp(char *a, char *b) { int len = 0; while(a[len] && b[len] && a[len] == b[len]) len++; return len; }

long long sum_all(char s[][300001], int n) { long long total = 0; for(int i = 0; i < n - 1; i++) { for(int j = i + 1; j < n; j++) { total += lcp(s[i], s[j]); } } return total; }

int main() { char s[300000][300001]; int n = read_input(s); printf("%lld\n", sum_all(s, n)); return 0; }
