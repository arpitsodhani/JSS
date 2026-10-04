#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void extract_substring(char *source, int start, int length, char *dest) {
    for (int i = 0; i < length; i++) {
        dest[i] = source[start + i];
    }
    dest[length] = '\0';
}

int check_substring_uniqueness(char substring[55], char seen[10005][55], int seen_count) {
    for (int i = 0; i < seen_count; i++) {
        if (strcmp(seen[i], substring) == 0) {
            return 0;
        }
    }
    return 1;
}

void register_unique_substring(char *substring, char seen[10005][55], int *seen_count) {
    strcpy(seen[*seen_count], substring);
    (*seen_count)++;
}

int enumerate_and_count_distinct_substrings(char *string) {
    int n = strlen(string);
    char seen[10005][55];
    int seen_count = 0;
    
    for (int start = 0; start < n; start++) {
        for (int length = 1; length <= n - start; length++) {
            char substring[55];
            extract_substring(string, start, length, substring);
            if (check_substring_uniqueness(substring, seen, seen_count)) {
                register_unique_substring(substring, seen, &seen_count);
            }
        }
    }
    return seen_count;
}

int main() {
    char string[100005];
    scanf("%s", string);
    printf("%d\n", enumerate_and_count_distinct_substrings(string));
    return 0;
}