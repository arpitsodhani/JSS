#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void compute_z_array_values(char *s, int n, int *z) {
    int left = 0, right = 0;
    z[0] = n;
    for (int i = 1; i < n; i++) {
        if (i > right) {
            left = right = i;
            while (right < n && s[right] == s[right - left]) {
                right++;
            }
            z[i] = right - left;
            right--;
        } else {
            int k = i - left;
            if (z[k] < right - i + 1) {
                z[i] = z[k];
            } else {
                left = i;
                while (right < n && s[right] == s[right - left]) {
                    right++;
                }
                z[i] = right - left;
                right--;
            }
        }
    }
}

int find_pattern_occurrences(char *pattern, char *text, int *positions) {
    char combined[200005];
    int z[200005];
    int p_len = strlen(pattern), t_len = strlen(text);
    sprintf(combined, "%s#%s", pattern, text);
    int total_len = strlen(combined);
    
    compute_z_array_values(combined, total_len, z);
    
    int count = 0;
    for (int i = p_len + 1; i < total_len; i++) {
        if (z[i] == p_len) {
            positions[count++] = i - p_len - 1;
        }
    }
    return count;
}

int main() {
    char pattern[100005], text[100005];
    int positions[100005];
    scanf("%s %s", pattern, text);
    
    int count = find_pattern_occurrences(pattern, text, positions);
    printf("%d\n", count);
    for (int i = 0; i < count; i++) {
        printf("%d ", positions[i]);
    }
    return 0;
}