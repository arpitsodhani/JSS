#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_string(int *n, int *k, char *s) {
    scanf("%d %d %s", n, k, s);
}

int check_has_k_palindrome(char *s, int n, int k) {
    for (int i = 0; i <= n - k; i++) {
        int is_pal = 1;
        for (int j = 0; j < k / 2; j++) {
            if (s[i + j] != s[i + k - 1 - j]) {
                is_pal = 0;
                break;
            }
        }
        if (is_pal) return 1;
    }
    return 0;
}

long long count_valid_permutations(char *s, int n, int k) {
    char perm[15];
    strcpy(perm, s);
    int used[15] = {0};
    long long count = 0;
    void generate(int pos) {
        if (pos == n) {
            if (!check_has_k_palindrome(perm, n, k)) count++;
            return;
        }
        for (int i = 0; i < n; i++) {
            if (used[i]) continue;
            perm[pos] = s[i];
            used[i] = 1;
            generate(pos + 1);
            used[i] = 0;
        }
    }
    generate(0);
    return count;
}

int main() {
    int n, k;
    char s[15];
    read_string(&n, &k, s);
    printf("%lld\n", count_valid_permutations(s, n, k));
    return 0;
}
