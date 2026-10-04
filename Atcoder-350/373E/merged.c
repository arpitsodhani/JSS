#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void compute_prefix_function(char *pattern, int m, int *prefix) {
    prefix[0] = 0;
    int k = 0;
    
    for (int i = 1; i < m; i++) {
        while (k > 0 && pattern[k] != pattern[i]) {
            k = prefix[k - 1];
        }
        if (pattern[k] == pattern[i]) {
            k++;
        }
        prefix[i] = k;
    }
}

int search_pattern_kmp(char *text, char *pattern, int *prefix, int *positions) {
    int n = strlen(text);
    int m = strlen(pattern);
    int count = 0, k = 0;
    
    for (int i = 0; i < n; i++) {
        while (k > 0 && pattern[k] != text[i]) {
            k = prefix[k - 1];
        }
        if (pattern[k] == text[i]) {
            k++;
        }
        if (k == m) {
            positions[count++] = i - m + 1;
            k = prefix[k - 1];
        }
    }
    return count;
}

int main() {
    char text[100005], pattern[100005];
    int prefix[100005], positions[100005];
    scanf("%s %s", text, pattern);
    
    int m = strlen(pattern);
    compute_prefix_function(pattern, m, prefix);
    int count = search_pattern_kmp(text, pattern, prefix, positions);
    
    printf("%d\n", count);
    for (int i = 0; i < count; i++) {
        printf("%d ", positions[i]);
    }
    return 0;
}