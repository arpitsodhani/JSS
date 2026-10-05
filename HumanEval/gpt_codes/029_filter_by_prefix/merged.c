#include <stdio.h>

void filter_by_prefix(char strs[][1000], int n, char *prefix, char result[][1000], int *result_len) {
    *result_len = 0;
    int prefix_len = strlen(prefix);
    for (int i = 0; i < n; i++) {
        int match = 1;
        for (int j = 0; j < prefix_len; j++) {
            if (strs[i][j] != prefix[j]) {
                match = 0;
                break;
            }
        }
        if (match) {
            strcpy(result[(*result_len)++], strs[i]);
        }
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    getchar();
    char strs[n][1000];
    for (int i = 0; i < n; i++) {
        fgets(strs[i], sizeof(strs[i]), stdin);
        strs[i][strcspn(strs[i], "\n")] = 0;
    }
    char prefix[1000];
    fgets(prefix, sizeof(prefix), stdin);
    prefix[strcspn(prefix, "\n")] = 0;
    char result[n][1000];
    int result_len;
    filter_by_prefix(strs, n, prefix, result, &result_len);
    for (int i = 0; i < result_len; i++) {
        printf("%s", result[i]);
        if (i < result_len - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
