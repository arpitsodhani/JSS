#include <stdio.h>
#include <string.h>

void read_input(int *n, int *k, char s[]) { scanf("%d%d", n, k); scanf("%s", s); }

int check_palindrome(char *str, int k) { for(int i = 0; i < k / 2; i++) { if(str[i] != str[k - 1 - i]) return 0; } return 1; }

long long count_good_strings(int n, int k, char s[]) { long long MOD = 998244353; long long dp[2005][2]; memset(dp, 0, sizeof(dp)); dp[0][0] = 1; for(int i = 0; i < n; i++) { for(int mask = 0; mask < (1 << k); mask++) { if(dp[i][0] == 0) continue; for(char c = 'A'; c <= 'B'; c++) { if(s[i] != '?' && s[i] != c) continue; int valid = 1; if(i >= k - 1) { char temp[2005]; for(int j = 0; j <= i; j++) temp[j] = s[j]; temp[i] = c; if(check_palindrome(temp + i - k + 1, k)) valid = 0; } if(valid) dp[i + 1][0] = (dp[i + 1][0] + dp[i][0]) % MOD; } } } return dp[n][0]; }

int main() { int n, k; char s[2005]; read_input(&n, &k, s); printf("%lld\n", count_good_strings(n, k, s)); return 0; }
