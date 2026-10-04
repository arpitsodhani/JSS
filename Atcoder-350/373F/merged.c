#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

long long compute_rolling_hash(char *s, int len, long long base, long long mod) {
    long long hash = 0;
    long long power = 1;
    for (int i = 0; i < len; i++) {
        hash = (hash + s[i] * power) % mod;
        power = (power * base) % mod;
    }
    return hash;
}

long long update_rolling_hash(long long old_hash, char old_char, char new_char, int len, long long base, long long mod, long long base_pow) {
    old_hash = (old_hash - old_char + mod) % mod;
    old_hash = (old_hash * base) % mod;
    old_hash = (old_hash + new_char * base_pow) % mod;
    return old_hash;
}

int search_pattern_rabin_karp(char *text, char *pattern, int *positions) {
    int n = strlen(text);
    int m = strlen(pattern);
    long long base = 31, mod = 1000000007;
    
    long long pattern_hash = compute_rolling_hash(pattern, m, base, mod);
    long long text_hash = compute_rolling_hash(text, m, base, mod);
    
    long long base_pow = 1;
    for (int i = 0; i < m - 1; i++) {
        base_pow = (base_pow * base) % mod;
    }
    
    int count = 0;
    for (int i = 0; i <= n - m; i++) {
        if (text_hash == pattern_hash) {
            int match = 1;
            for (int j = 0; j < m; j++) {
                if (text[i + j] != pattern[j]) {
                    match = 0;
                    break;
                }
            }
            if (match) positions[count++] = i;
        }
        
        if (i < n - m) {
            text_hash = update_rolling_hash(text_hash, text[i], text[i + m], m, base, mod, base_pow);
        }
    }
    return count;
}

int main() {
    char text[100005], pattern[100005];
    int positions[100005];
    scanf("%s %s", text, pattern);
    
    int count = search_pattern_rabin_karp(text, pattern, positions);
    printf("%d\n", count);
    for (int i = 0; i < count; i++) {
        printf("%d ", positions[i]);
    }
    return 0;
}