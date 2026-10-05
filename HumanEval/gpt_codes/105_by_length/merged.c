#include <stdio.h>
#include <string.h>

void sort_by_length(char words[][100], int n, char result[][100], int *result_len) {
    int lengths[n];
    for (int i = 0; i < n; i++) {
        lengths[i] = strlen(words[i]);
    }
    *result_len = 0;
    for (int target_len = 9; target_len >= 1; target_len--) {
        for (int i = 0; i < n; i++) {
            if (lengths[i] == target_len) {
                strcpy(result[(*result_len)++], words[i]);
            }
        }
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    char words[n][100];
    for (int i = 0; i < n; i++) {
        scanf("%s", words[i]);
    }
    char result[n][100];
    int result_len;
    sort_by_length(words, n, result, &result_len);
    for (int i = 0; i < result_len; i++) {
        printf("%s", result[i]);
        if (i < result_len - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
