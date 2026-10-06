#include <stdio.h>
#include <string.h>

void sort_by_length(int values[], int n, char result[][10], int *result_len) {
    static const char *names[] = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
    *result_len = 0;
    for (int target_len = 9; target_len >= 1; target_len--) {
        for (int i = 0; i < n; i++) {
            if (values[i] == target_len) {
                strcpy(result[(*result_len)++], names[target_len]);
            }
        }
    }
}

int main(void) {
    int n;
    scanf("%d", &n);
    int values[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &values[i]);
    }
    char result[n][10];
    int result_len;
    sort_by_length(values, n, result, &result_len);
    for (int i = 0; i < result_len; i++) {
        printf("%s", result[i]);
        if (i < result_len - 1) printf(" ");
    }
    printf("\n");
    return 0;
}
